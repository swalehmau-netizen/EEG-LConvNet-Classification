# EEG-LConvNet-Classification
LConvNet: A CNN-LSTM architecture for EEG epileptiform classification
LConvNet is a deep learning architecture designed for EEG-based epileptiform classification.
The model integrates convolutional feature extraction with temporal modeling to capture spatial and temporal EEG dynamics across multiple channels.
This repository provides the implementation used in the publication: 

Author: Swaleh Omar et. al
Title: Enhancing EEG signals classification using LSTM-CNN architecture
Journal: Engineering Reports
Year: 2023
URL: https://onlinelibrary.wiley.com/doi/10.1002/eng2.12827

# Model Architecture  
<img width="707" height="506" alt="Picture1" src="https://github.com/user-attachments/assets/e91458f5-1ba9-4516-a95b-6c250c1f7d28" />

# Key Contributions
• Proposed LConvNet architecture for EEG classification
• Integration of convolutional and temporal modeling
• Extraction of spatial and temporal EEG features
• Improved epileptiform pattern detection

# Input Data Format
EEG input shape: (256, 25)

256 → time samples  
25 → EEG channels

# Installation
pip install -r requirements.txt

# Training the Model
python training/train_model.py

# Evaluation
python evaluation/evaluate_model.py

# Requirements
• tensorflow
• numpy
• scipy
• matplotlib
• scikit-learn
• mne
• pandas

## Citation

If you use this work, please cite:

Omar, S. M., Kimwele, M., Olowolayemo, A., & Kaburu, D. M. (2024). Enhancing EEG signals classification using LSTM-CNN architecture. Engineering Reports, 6, e12827.
  number={9},
  pages={e12827},
  year={2024},
  publisher={Wiley Online Library}
}
