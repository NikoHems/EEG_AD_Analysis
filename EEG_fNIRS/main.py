from dataloader import EEGData



def main():
    eeg_data = EEGData(root='../csv_folder/Experiment1')
    eeg_data.read_data(file_name='RFECV-5secEEGPSD_FullFnirsPSD_FullFnirsTimeDomain_R-C1-C2-N1-N2-V.csv')

    X, y = next(iter(eeg_data.train_dataloader()))
    print('-'*20)
    print('>>> X shape:', X.shape, '\ny shape:', y.shape)


if __name__ == '__main__':
    main()

