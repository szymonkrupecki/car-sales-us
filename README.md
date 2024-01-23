# car-sales-us

## Introduction/Overview

The application utilizes a dataset on car sales advertisements, 
allowing users to interactively explore 
and analyze various aspects of vehicle data. 

## Features

- Interactive data visualizations using Plotly Express.
- Dynamic controls for data exploration, including sliders and checkboxes.
- Real-time updates of visualizations based on user input.
- Responsive design for ease of use across different devices.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly Express

## Link to the app on render:
https://car-sales-us-app.onrender.com/

The app is unfortunatelly not running. I am getting this code error:
 
`ERROR: Could not build wheels for numpy, which is required to install pyproject.toml-based projects
      Failed to build numpy
        ERROR: Failed building wheel for numpy
        note: This error originates from a subprocess, and is likely not a problem with pip.
            error: Command "gcc -pthread -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNPY_INTERNAL_BUILD=1 -DHAVE_NPY_CONFIG_H=1 -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE=1 -D_LARGEFILE64_SOURCE=1 -DNO_ATLAS_INFO=1 -DHAVE_CBLAS -I/usr/local/include -I/usr/include -I/opt/render/project/src/.venv/include -Ibuild/src.linux-x86_64-3.11/numpy/core/src/umath -Ibuild/src.linux-x86_64-3.11/numpy/core/src/npymath -Ibuild/src.linux-x86_64-3.11/numpy/core/src/common -Inumpy/core/include -Ibuild/src.linux-x86_64-3.11/numpy/core/include/numpy -Inumpy/core/src/common -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/src/npysort -I/opt/render/project/src/.venv/include -I/usr/local/include/python3.11 -Ibuild/src.linux-x86_64-3.11/numpy/core/src/common -Ibuild/src.linux-x86_64-3.11/numpy/core/src/npymath -c build/src.linux-x86_64-3.11/numpy/core/src/multiarray/scalartypes.c -o build/temp.linux-x86_64-3.11/build/src.linux-x86_64-3.11/numpy/core/src/multiarray/scalartypes.o -MMD -MF build/temp.linux-x86_64-3.11/build/src.linux-x86_64-3.11/numpy/core/src/multiarray/scalartypes.o.d -std=c99" failed with exit status 1
`

## Installation and Setup

```bash
pip install streamlit pandas plotly
streamlit run app.py

