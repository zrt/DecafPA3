VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T4 = "pa1"
    _T5 = 2
    _T6 = 0
    _T7 = (_T5 < _T6)
    if (_T7 == 0) branch _L10
    _T8 = "Decaf runtime error: The length of the created array should not be less than 0.\n"
    parm _T8
    call _PrintString
    call _Halt
_L10:
    _T9 = 4
    _T10 = (_T9 * _T5)
    _T11 = (_T9 + _T10)
    parm _T11
    _T12 =  call _Alloc
    *(_T12 + 0) = _T5
    _T12 = (_T12 + _T11)
_L11:
    _T11 = (_T11 - _T9)
    if (_T11 == 0) branch _L12
    _T12 = (_T12 - _T9)
    *(_T12 + 0) = _T4
    branch _L11
_L12:
    _T3 = _T12
    _T14 = 0
    _T15 = "pa2"
    _T16 = 4
    _T17 = (_T14 * _T16)
    _T18 = (_T3 + _T17)
    _T19 = *(_T3 - 4)
    _T20 = 4
    parm _T20
    _T21 =  call _Alloc
    _T22 = (_T14 < _T19)
    if (_T22 == 0) branch _L13
    _T23 = 0
    _T24 = (_T14 < _T23)
    if (_T24 == 0) branch _L14
_L13:
    *(_T21 + 0) = _T15
    _T25 = 0
    if (_T25 == 0) branch _L15
_L14:
    _T26 = *(_T18 + 0)
    *(_T21 + 0) = _T26
_L15:
    _T27 = *(_T21 + 0)
    _T13 = _T27
    _T29 = 2
    _T30 = "pa3"
    _T31 = 4
    _T32 = (_T29 * _T31)
    _T33 = (_T3 + _T32)
    _T34 = *(_T3 - 4)
    _T35 = 4
    parm _T35
    _T36 =  call _Alloc
    _T37 = (_T29 < _T34)
    if (_T37 == 0) branch _L16
    _T38 = 0
    _T39 = (_T29 < _T38)
    if (_T39 == 0) branch _L17
_L16:
    *(_T36 + 0) = _T30
    _T40 = 0
    if (_T40 == 0) branch _L18
_L17:
    _T41 = *(_T33 + 0)
    *(_T36 + 0) = _T41
_L18:
    _T42 = *(_T36 + 0)
    _T28 = _T42
    parm _T13
    call _PrintString
    parm _T28
    call _PrintString
}

