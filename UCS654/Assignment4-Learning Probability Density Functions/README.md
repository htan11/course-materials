## Methodology

### Roll-Number-Parameterized Transformation

The original feature \(x\) (NO₂ concentration) is transformed into a new variable \(z\) using a roll-number-dependent non-linear function:


$$z = T_r(x) = x + a_r \cdot \arcsin(b_r x)$$

where the parameters are defined as:

$$a_r = 0.5 \times (r \bmod 7), \quad b_r = 0.3 \times (r \bmod 5 + 1)$$


For roll number **102303812**, the values are:

$$a_r = 1.0,\quad b_r = 0.9$$

Resulting transformation:

$$z = x + \arcsin(0.9x)$$

To ensure mathematical validity, the input to the arcsin function is clipped to the interval $$[-1,1]$$, and invalid values are removed.

---

### PDF Modeling Using GAN

The probability density function of the transformed variable $$z$$ is assumed to be unknown. No parametric distribution is assumed. A Generative Adversarial Network (GAN) is used to learn the distribution directly from samples.

The generator maps random noise sampled from a standard normal distribution to synthetic samples of $$z$$, while the discriminator attempts to distinguish between real and generated samples. Through adversarial training, the generator learns to approximate the true data distribution.

![Alt text] (UCS654/Assignment4-Learning Probability Density Functions/code/plot.png)

---

### PDF Approximation from Generator Samples

After training, a large number of samples are generated from the generator. These samples are used to estimate the probability density function $$(\hat{p}_h(z)\)$$ using Kernel Density Estimation (KDE). The resulting density represents the GAN-learned approximation of the unknown PDF.

