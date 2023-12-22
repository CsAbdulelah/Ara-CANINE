# Ara-CANINE: Arabic Language Model


## Model Description

**Ara-CANINE** is a character-based, pre-trained language model specifically developed for the Arabic language. Unlike traditional models that rely on sub-word tokenization, Ara-CANINE utilizes a free-tokenization method, processing raw characters without explicit tokenization. This approach allows the model to effectively capture the nuances of Arabic, including its various dialects and colloquial forms.

## Training Data

Ara-CANINE was pre-trained on the QADI dialects tweets dataset, which includes tweets in 18 Arabic dialects, totaling 40GB of text data. The training was conducted for 40 epochs on 3 A100 GPUs, using the DeepSpeed library to optimize the training process.

## Evaluation

The model's performance was evaluated using the Arabic Language Understanding Evaluation (ALUE) benchmark, consisting of eight diverse tasks that test various aspects of language understanding, such as sentiment analysis, text categorization, and dialect detection.

## Results

Ara-CANINE demonstrates competitive performance compared to existing Arabic language models on the ALUE benchmark. It particularly excels in tasks involving dialects and social media text, attributed to its training on dialect-rich datasets. The model shows promise in specific linguistic contexts and has outperformed several larger models in certain tasks.

## Usage

Ara-CANINE can be used for a variety of NLP tasks involving the Arabic language, including but not limited to sentiment analysis, dialect detection, and text classification.

## Availability

The source code and model checkpoints for Ara-CANINE will be made publicly available on our GitHub repository, facilitating replication of experiments and further research in Arabic NLP.

GitHub Repository: [Ara-CANINE GitHub](https://github.com/CsAbdulelah/Ara-CANINE.git)

## Citation

If you use Ara-CANINE in your research, please cite our paper.
# How to cite this work

There is no paper associated with SHIBA, but the repository can be cited like this:

```bibtex
@misc{shiba,
  author = {Joshua Tanner and Masato Hagiwara},
  title = {SHIBA: Japanese CANINE model},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/octanove/shiba}},
}
```

Please also cite the original CANINE paper:
```bibtex
@misc{clark2021canine,
      title={CANINE: Pre-training an Efficient Tokenization-Free Encoder for Language Representation}, 
      author={Jonathan H. Clark and Dan Garrette and Iulia Turc and John Wieting},
      year={2021},
      eprint={2103.06874},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact

For questions or support regarding Ara-CANINE, please contact us at:

- Email: [csabdulelah@gmail.com](mailto:csabdulelah@gmail.com)

## Acknowledgments

This work was inspired by Shiba, and CANINE,  I would thank Joshua Tanner and Masato Hagiwara for their efforts in publically implementing a CANINE model which is the base for this work [Shiba GitHub](https://github.com/octanove/shiba.git) This work was supported by the High-Performance Computing (HPC) Center at King Abdulaziz University, particularly the Aziz Supercomputer.









---
license: apache-2.0
---

