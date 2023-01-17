import cowskit

dataset = cowskit.datasets.IrisDataset(
    path = "./quantumAI/cowskit/files/iris.dataset",# cowskit.files.IRIS_DATASET,
)

encoding = cowskit.encodings.AngleEncoding(dataset=dataset)

model = cowskit.models.ConvolutionalModel(
    dataset=dataset, 
    encoding=encoding
)

model.infer()

