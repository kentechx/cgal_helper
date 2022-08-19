# cgal_helper
```
sudo apt install libcgal-dev libeigen3-dev
git clone https://github.com/cgal/cgal-swig-bindings && cd cgal-swig-bindings && git checkout 422c3e2a3230e478dd609e1dc44d6529e2bc963d
mkdir build -p && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCGAL_DIR=/usr/lib/x86_64-linux-gnu/cmake/CGAL -DBUILD_JAVA=OFF -DPYTHON_OUTDIR_PREFIX=../examples/python ..
make -j 4
cd ../examples/python
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:lib
```
