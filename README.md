---
# 0x9 Generator
## Motivation
To train a vanilla generative adversarial network to generate images from 0 to 9
## Requirements
Python 3.8 or above with all [requirements](requirements.txt) dependencies installed. To install run:
```python
$ pip3 install -r requirements.txt
```
## To run
```python
$ streamlit run digitgenerator.py
```
## Examples

#### After 10 epochs: 

<img src="https://user-images.githubusercontent.com/52780573/102694930-38a0af80-424a-11eb-9031-ab9da9602d81.png" data-canonical-src="" width="800" height="500" />

#### After 100 epochs: 

<img src="https://user-images.githubusercontent.com/52780573/102694936-40f8ea80-424a-11eb-8e05-0308be7a9d0e.png" data-canonical-src="" width="800" height="500" />

#### After 200 epochs: 

<img src="https://user-images.githubusercontent.com/52780573/102694938-46563500-424a-11eb-83db-a1cd21a57c39.png" data-canonical-src="" width="800" height="500" />

#### After 300 epochs: 

<img src="https://user-images.githubusercontent.com/52780573/102694939-49512580-424a-11eb-9902-52ab7547a704.png" data-canonical-src="" width="800" height="500" />

#### After 399 epochs: 

<img src="https://user-images.githubusercontent.com/52780573/102694943-4bb37f80-424a-11eb-9b5b-214d07ffb7c5.png" data-canonical-src="" width="800" height="500" />

## Might Do
- [ ] Make it deployable, currently the images generated are being shown through matplotlib which isn't all that suited for deployment

---
