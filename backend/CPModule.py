class CPModule(pl.LightningDataModule):
    def __init__(self, x_train, y_train, x_val, y_val, x_test, y_test, batch_size = 16):
        super().__init__()
        self.train_text = x_train
        self.train_label = y_train
        self.val_text = x_val
        self.val_label = y_val
        self.test_text = x_test
        self.test_label = y_test
        self.batch_size = batch_size

    def setup(self, stage = None):
        self.train_dataset = CPProblemsDataset(texts = self.train_text, labels = self.train_label)
        self.val_dataset = CPProblemsDataset(texts = self.val_text, labels = self.val_label)
        self.test_dataset = CPProblemsDataset(texts = self.test_text, labels = self.test_label)
        
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size = self.batch_size, shuffle = True, num_workers = 2)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size = 16)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size = 16)
