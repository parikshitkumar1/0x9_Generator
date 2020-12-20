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
>>or check it out here: https://thisdigitprobablyexists.herokuapp.com/
## Examples

#### was trained for 400 epochs

<img src="https://user-images.githubusercontent.com/52780573/102699440-b2e12c00-426a-11eb-8198-7a76db824743.gif" data-canonical-src="" width="800" height="500" />

<img src="https://user-images.githubusercontent.com/52780573/102704942-d2e31080-42a7-11eb-84a9-630444f33c87.png" data-canonical-src="" width="800" height="500" />

<img src="https://user-images.githubusercontent.com/52780573/102704947-e68e7700-42a7-11eb-9f6e-f8653e8c103f.png" data-canonical-src="" width="800" height="500" />

<img src="https://user-images.githubusercontent.com/52780573/102704955-02921880-42a8-11eb-9e7d-0525102f748b.png" data-canonical-src="" width="800" height="500" />

<img src="https://user-images.githubusercontent.com/52780573/102704964-1f2e5080-42a8-11eb-8002-f308e8ebba57.png" data-canonical-src="" width="800" height="500" />

<img src="https://user-images.githubusercontent.com/52780573/102704981-64eb1900-42a8-11eb-88d5-a33d81a1dfe5.png" data-canonical-src="" width="800" height="500" />
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
