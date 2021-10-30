# test-qt

1. 通过vcpkg安装qt5.
```
vcpkg install qt5
```

2. 设置cmake-kits.

在Win11上需要额外安装Win11 SDK, 不然cmake configure时会出现
`cannot find valid CXX compiler`
具体为链接失败, 找不到`ucrt.lib`.
