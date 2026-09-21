import cvxpy as cp
import matplotlib.pyplot as plt

if __name__ == '__main__':

    N = 24
    SOC_initial = 0.2
    SOC_min = 0.2
    SOC_max = 0.8
    dt = 1
    E_bat = 60
    P_charge_max = 5
    P_discharge_max = 5
    P_grid_max = 5.0
    c_buy = 50

    SOC = cp.Variable(N)
    P_bat = cp.Variable(N)
    P_grid = cp.Variable(N)
    P_load = cp.Variable(N)
    P_pv = cp.Variable(N)

    # початкове значення заряду
    constraints = [
        SOC[0] == SOC_initial
    ]

    for t in range(N - 1):
        # реалізація заряду батареї
        constraints += [
            SOC[t + 1] ==
            SOC[t] - P_bat[t] * dt / E_bat
        ]

    # обмеження на рівень заряду батареї
    constraints += [
        SOC >= SOC_min,
        SOC <= SOC_max,
        P_bat >= -P_charge_max,
        P_bat <= P_discharge_max,
    ]

    # рівняння балансу
    P_grid = P_load - P_pv - P_bat

    # обмеження на імпорт електроенергії з централізованого джерела
    constraints += [
        P_grid <= P_grid_max,
        P_grid >= 0
    ]

    # обмеження на PV-генерацію
    constraints += [
        P_pv >= 0,
        P_pv[0] == 0,
        P_pv[1] == 0,
        P_pv[2] == 0,
        P_pv[3] == 0,
        P_pv[4] == 0,
        P_pv[5] == 0,
        P_pv[21] == 0,
        P_pv[22] == 0,
        P_pv[23] == 0,
        P_pv[12] == 5,
        P_pv[13] == 5
    ]

    # обмеження на попит (він завжди є впродовж доби)
    constraints += [
        P_load >= 0
    ]

    cost = cp.sum(
        cp.multiply(c_buy, P_grid)
    ) * dt

    problem = cp.Problem(cp.Minimize(cost), constraints)

    problem.solve()
    print(problem.status)
    print("SOC:")
    print(SOC.value)
    print("P_bat:")
    print(P_bat.value)
    print("P_pv:")
    print(P_pv.value)
    print("P_load:")
    print(P_load.value)
    print("P_grid:")
    print(P_grid.value)

    print("cost" + str(cost.value))
    plt.style.use('tableau-colorblind10')

    f1 = plt.figure()

    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], SOC.value)

    plt.xlabel("Час доби", fontsize=16)
    plt.ylabel("Рівень заряду", fontsize=16)
    plt.legend(['N = ' + str(N)])
    plt.title('Рівень заряду батареї (SOC)', fontsize=20)
    plt.show()

    f2 = plt.figure()
    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_pv.value, P_load.value)
    plt.xlabel("Час доби", fontsize=16)
    plt.ylabel("Потужність, кВт", fontsize=16)
    plt.legend(['P_pv', 'P_load'])
    plt.title('Генерація/споживання', fontsize=20)
    plt.show()

    #f3 = plt.figure()
    #plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_grid.value)
    #plt.xlabel("Час доби", fontsize=16)
    #plt.ylabel("Потужність, кВт", fontsize=16)
    #plt.legend(['P_grid'])
    #plt.title('Імпорт з централізованого джерела', fontsize=20)
    #plt.show()