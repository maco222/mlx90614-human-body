MLX90614 Human Body 
===================

Human body temperature estimation using Melexis MLX90614-DCI sensor, AdafruitFT232H board and according to US Patent (expired) US6299347B1. 

Instalation
===========

.. code-block:: shell

    sudo pip3 install git+https://github.com/maco222/mlx90614-human-body

Usage Example
=============

Run example with this env variable:

.. code-block:: shell

    sudo BLINKA_FT232H=1 python3 examples/single_read.py