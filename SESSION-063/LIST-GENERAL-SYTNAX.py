Concat:
    s = s1 + s2
    L = L1 + L1
    T = T1 + T2

Multiplication by scaler
    s1 = s * n
    L1 = L * n
    T1 = T * n

Index operator
    s1 = s[i]
    n = L[i]
    p = T[i]

Range Operator
    s1 = s[i : j]
    L1 = L[i : j]
    T1 = T[i:j]

Range with anchor
    s1 = s[:i]
    L1 = L[i:]
    T1=  T[:]

Slice Operator
    s1 = s[i : j : k]
    L1 = L[i : j : k]
    T1 = T[i : j : k]

Slice with anchor
    s1 = s[i::k]
    L1 = L[:j:k]
    T1 = T[::k]

Index method
    n = s.index(sub_string, start_index)
    n = L.index(element, start_index)
    n = T.index(element, start_index)

Count method
    n = s.count(sub_string)
    n = L.count(element)
    n = T.count(element)

    n = s[::-1].count(sub_string)
    
