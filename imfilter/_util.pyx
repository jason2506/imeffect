import numpy as np
cimport numpy as np


cdef inline np.double_t _lerp(np.double_t a, np.double_t b, np.double_t t):
    return a * (1 - t) + b * t


cdef np.ndarray[np.int_t, ndim=1] _fill_missing_values(dict values, int end):
    cdef np.ndarray[np.double_t, ndim=1] result
    cdef unsigned int i, j
    cdef tuple left, right
    cdef double offset

    result = np.zeros(end + 1)
    for i in xrange(end + 1):
        if i in values:
            result[i] = values[i]
        elif i > 0:
            left = (i - 1, result[i - 1])
            right = None
            for j in xrange(i, end + 1):
                if j in values:
                    right = (j, values[j])
                    break

            if right is None:
                result[i:end + 1] = result[i - 1]
                break

            offset = (right[1] - left[1]) / (right[0] - left[0]) * (i - left[0])
            result[i] = left[1] + offset

    return np.round(result).astype(np.int)


cpdef np.ndarray[np.int_t, ndim=1] bezier(np.ndarray[np.int_t, ndim=2] cps,
                                          int lower=0, int upper=255):
    cdef dict result
    cdef unsigned int i, j, k
    cdef double t, val
    cdef int idx, end
    cdef np.ndarray[np.double_t, ndim=2] p

    result = {}
    for i in xrange(1000):
        t = i * 0.001
        p = np.copy(cps).astype(np.float)
        for j in xrange(p.shape[0] - 1, 0, -1):
            for k in xrange(j):
                p[k, 0] = _lerp(p[k, 0], p[k + 1, 0], t)
                p[k, 1] = _lerp(p[k, 1], p[k + 1, 1], t)

        idx = int(round(p[0, 0]))
        val = min(max(p[0, 1], lower), upper)
        result[idx] = round(val)

    end = cps[-1][0]
    return _fill_missing_values(result, end)


cpdef np.ndarray choose(np.ndarray a, np.ndarray choices, np.ndarray out):
    cdef int idx, val
    for idx, val in enumerate(choices):
        out[a == idx] = val

    return out
