## About
Simple coin toss simulator written in our good friend `Python`.

## Usage
```
$ python flipcoin.py <flips> <games>
```

## Example
```
$ python flipcoin.py 10 10
----------
[[ 1.  0.  1.  0.  1.  0.  0.  0.  1.  1.]
 [ 1.  0.  1.  1.  0.  1.  0.  0.  1.  0.]
 [ 1.  1.  0.  1.  0.  1.  0.  1.  0.  1.]
 [ 0.  0.  1.  0.  1.  1.  0.  0.  0.  1.]
 [ 1.  0.  0.  1.  1.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.  1.  0.  1.]
 [ 1.  0.  0.  1.  0.  0.  0.  0.  1.  0.]
 [ 1.  0.  1.  0.  1.  1.  1.  0.  1.  0.]
 [ 0.  1.  0.  0.  1.  1.  1.  1.  1.  0.]
 [ 0.  1.  1.  1.  0.  1.  1.  0.  0.  0.]]
----------
Heads = 47
Tails = 53
Percentage heads = 47.0%
```

The above `M x N` matrix is the result of `flips x games`.
