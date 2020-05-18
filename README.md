# gallimaufry

Assortment of useful scripts and commands


## generate_primitive_gif

Used to make "images come to life".


### Prerequisites

- [Primitive](https://github.com/fogleman/primitive)

### Usage

```bash
askew.py [-i image_path] [-o outout] [--mode] [--theta] [--phi] [--gamma] [--length] [--width] [--dx] [--dy] [--dz]
```

```bash
python3 generate_primitive_gif.py 5000,5000,5000,5000 data/Night_Parliament.jpg output/Parliament.png
```

Single image:

```bash
python3 askew.py -i images/example.jpg --mode single  --theta 120 --gamma 120  --dz 10
```

### Animation

"Focusing" GIF:

![](output/output.gif)

"Shimmering" GIF:

![](output/Night_Time_Parliament.gif)

### Acknowledgments

Fogelman made primitive. 