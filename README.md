This is a paper interpretation project where I take a technical paper and implement it in Pytorch or Tensorflow
# Siamese networks for facial comparison
Facial comparison using Siamese Networks

## Paper
This is the Pytorch interpretation of the paper [Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) submitted to ICML deep learning workshop, vol. 2. 2015. 2015 

The network does not learn to classify an image directly to any of the output classes. Rather, it is learning a similarity function, which takes two images as input and expresses how similar they are.

Instead of directly classifying an input(test) image to one of the 10 people in the organization, this network instead takes an extra reference image of the person as input and will produce a similarity score denoting the chances that the two input images belong to the same person. 
Hence, if we consider one person as a single class, we need only one training example for each person.

## Data
[Labeled Faces in the Wild (LFW)](http://vis-www.cs.umass.edu/lfw/) is a database of face photographs designed for studying the problem of unconstrained face recognition. This database was created and maintained by researchers at the University of Massachusetts, Amherst (specific references are in Acknowledgments section). 13,233 images of 5,749 people were detected and centered by the Viola Jones face detector and collected from the web. 1,680 of the people pictured have two or more distinct photos in the dataset. The original database contains four different sets of LFW images and also three different types of "aligned" images. According to the researchers, deep-funneled images produced superior results for most face verification algorithms compared to the other image types. Hence, the dataset uploaded here is the deep-funneled version.

Link to tar file - http://vis-www.cs.umass.edu/lfw/lfw.tgz

## Reference
[Gary B. Huang](http://vis-www.cs.umass.edu/~gbhuang), Manu Ramesh, [Tamara Berg](http://research.yahoo.com/bouncer_user/83), and [Erik Learned-Miller](http://www.cs.umass.edu/~elm).
<br><b>Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments.</b>
<i>University of Massachusetts, Amherst, Technical Report 07-49, October, 2007.</i>
[pdf](http://vis-www.cs.umass.edu/lfw/lfw.pdf)
