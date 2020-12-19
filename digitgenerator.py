from torchvision import models, transforms
import torch
from PIL import Image
import torch.nn as nn
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import streamlit as st


st.title("Digit Generator")

st.write("This is a generative adversarial network trained on the MNIST dataset for 400 epochs")

st.write("make sure to close the matplotlib popup before reloading for a new digit, in case no digit pops up, please re-run the app")

st.write("After 10 epochs: ")

st.markdown("![10](https://user-images.githubusercontent.com/52780573/102694930-38a0af80-424a-11eb-9031-ab9da9602d81.png)")

st.write("After 100 epochs: ")

st.markdown("![fake_images-0100](https://user-images.githubusercontent.com/52780573/102694936-40f8ea80-424a-11eb-8e05-0308be7a9d0e.png)")

st.write("After 200 epochs: ")

st.markdown("![fake_images-0200](https://user-images.githubusercontent.com/52780573/102694938-46563500-424a-11eb-83db-a1cd21a57c39.png)")

st.write("After 300 epochs: ")

st.markdown("![300](https://user-images.githubusercontent.com/52780573/102694939-49512580-424a-11eb-9902-52ab7547a704.png)")

st.write("After 399 epochs: ")

st.markdown("![400](https://user-images.githubusercontent.com/52780573/102694943-4bb37f80-424a-11eb-9b5b-214d07ffb7c5.png)")





G = torch.load("Gf.pth", map_location = "cpu")

G.eval()

def denorm(x):
	    out = (x + 1) / 2
	    return out.clamp(0, 1)

latent_size = 64
batch_size = 100

def new():
	device = torch.device('cpu')
	G.to(device);

	G.to(device);
	y = G(torch.randn(1, latent_size))
	gen_imgs = denorm(y.reshape((-1, 32,32)).detach())

	plt.imshow(gen_imgs[0], cmap='plasma');
	plt.show()



new()







