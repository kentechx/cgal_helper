# cgal_helper
```
git clone https://github.com/cgal/cgal-swig-bindings
cd cgal-swig-bindings
mkdir build -p && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCGAL_DIR=/usr/lib/CGAL -DBUILD_JAVA=OFF -DPYTHON_OUTDIR_PREFIX=../examples/python ..
make -j 4
cd ../examples/python
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:lib
```
