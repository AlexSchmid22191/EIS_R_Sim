from numpy import exp, sqrt, square, array, vectorize, log
from scipy.constants import physical_constants

e = physical_constants['elementary charge'][0]
k = physical_constants['Boltzmann constant'][0]
R = physical_constants['molar gas constant'][0]

T = 873.14      # Experiment temperature 600°C
c = 1.665e22    # Concentration of unit cells


def residual_function(x, *args):
    """Defect chemical system of LSF, charge balance, intrinsic and oxygen exchange equilibrium, cube root law

    :param x: defect concentrations per unit cell
    :type x: tuple

    :param args: pressure, jv, jh, ki, kox
    :type args: float

    """
    xv, xh, xe = x
    p, ki, kox = args
    res_charge = 2*xv+xh-xe-0.4
    res_intrinsic = xe*xh-ki*square(1-xh-xe)
    res_exchange = square(xh)*(3-xv)-kox*square(1-xe-xh)*xv*sqrt(p)
    residual = array([res_charge, res_intrinsic, res_exchange])
    return residual


def residual_jacobian(x, *args):
    """Jacobian of the LSF defect equation system, cube root law
    :param x: defect concentrations per unit cell
    :type x: tuple

    :param args: pressure, jv, jh, ki, kox
    :type args: float

    """
    xv, xh, xe = x
    p, ki, kox = args
    f_charge_xv = 2
    f_charge_xh = 1
    f_charge_xe = -1
    f_intrinsic_xv = 0
    f_intrinsic_xh = 2*ki*(1-xe-xh) + xe
    f_intrinsic_xe = 2*ki*(1-xe-xh) + xh
    f_exchange_xv = -kox*sqrt(p)*square(1-xe-xh) - square(xh)
    f_exchange_xh = -kox*sqrt(p)*xv*(2*xe + 2*xh - 2) + 2*xh*(-xv + 3)
    f_exchange_xe = -kox*sqrt(p)*xv*(2*xe + 2*xh - 2)

    jacobian = array([[f_charge_xv, f_charge_xh, f_charge_xe],
                      [f_intrinsic_xv, f_intrinsic_xh, f_intrinsic_xe],
                      [f_exchange_xv, f_exchange_xh, f_exchange_xe]])

    return jacobian


def oxygenpot(eta, p):
    """
    Calculate oxygen potential vs 1 bar oxygen

    :param eta: Overpotential in V
    :type eta: float

    :param p: Pressure in mbar
    :type p: float

    """

    opot = 2*eta + k*T/2/e * log(p)

    return opot


oxygenpot = vectorize(oxygenpot)


def equi_pressure(opot):
    """
    Calculate equivalent oxygen partial pressure in bar

    :param opot: Oxygen potential vs a bar in V
    :type opot: float

    """
    equip = exp(2*e*opot/k/T)

    return equip


equi_pressure = vectorize(equi_pressure)

