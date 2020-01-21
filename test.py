import torch
from utils import parse_args
from torch.autograd import Variable
from torchvision import transforms
from pathlib import Path
import pandas as pd
from PIL import Image


#args = parse_args()
CUDA_DEVICES = 2#args.cuda_devices
DATASET_ROOT = './test'#args.path
PATH_TO_WEIGHTS = './model-0.83-best_train_acc.pth'#args.weight


def test():
    data_transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    dataset_root = Path(DATASET_ROOT)
    classes = [_dir.name for _dir in Path('./train').glob('*')]

    model = torch.load(PATH_TO_WEIGHTS)
    model = model.cuda(CUDA_DEVICES)
    model.eval()

    sample_submission = pd.read_csv(str(dataset_root.joinpath('sample_submission.csv')))
    submission = sample_submission.copy()
    for i, filename in enumerate(sample_submission['file']):
        image = Image.open(Path(DATASET_ROOT).joinpath(filename)).convert('RGB')
        image = data_transform(image).unsqueeze(0)
        inputs = Variable(image.cuda(CUDA_DEVICES))
        outputs = model(inputs)
        _, preds = torch.max(outputs.data, 1)

        submission['species'][i] = classes[preds[0]]

    submission.to_csv(("./sample_submission.csv"), index=False)



if __name__ == '__main__':
    test()
