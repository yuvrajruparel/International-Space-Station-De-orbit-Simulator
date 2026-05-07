def euler(accel, vel_init, pos_init, delta_t=1.):
    """
    Does euler approximation once in one dimension.
    You will need to call for x and y.
    """
    vel = vel_init
    pos = pos_init
    vel_next = vel + accel * delta_t
    pos_next = pos + vel * delta_t
    return vel_next, pos_next