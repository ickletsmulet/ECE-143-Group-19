def train(model,loader_train, loader_validation,device,optimizer, dtype,epochs,print_process=True):
    """
    Inputs:
    - model: A PyTorch Module giving the model to train.
    - optimizer: An Optimizer object we will use to train the model
    - epochs: (Optional) A Python integer giving the number of epochs to train for
    
    Returns: Nothing, but prints model accuracies during training.
    """
    import torch
    import torch.nn as nn
    import torch.optim as optim
    import torch.nn.functional as F
    import numpy as np
    model = model.to(device=device)  # move the model parameters to CPU/GPU
    best_val_loss = None
    his_tra = []
    his_val = []
    his_epoch = []
    for e in range(epochs):
        loss_perepoch = 0

        for t, content in loader_train.items():
            model.train()  # put model to training mode
            # x is the features and y is the win rate
            x = content[0]
            y = content[1]

            x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
            y = y.to(device=device, dtype=torch.float)

            PER_C = model(x)
            # Loss is the mean square error
            #logistic or not, l have not tried yet
            F.sigmoid(PER_C)
            win_rate = sum(PER_C)
            criterion =nn.MSELoss()

            loss = criterion(win_rate, y)
            loss_perepoch += loss
            # Zero out all of the gradients for the variables which the optimizer
            # will update.
            optimizer.zero_grad()

            # This is the backwards pass: compute the gradient of the loss with
            # respect to each  parameter of the model.
            loss.backward()

            # Actually update the parameters of the model using the gradients
            # computed by the backwards pass.
            optimizer.step()

            #if time % print_every == 0:
             #   print(loss[0])
              #  print()


            if print_process==True:
                print('now we have')
                print(t,win_rate,y)
        # every ten epochs print the loss on validation set
        
        if e%10 == 0:
            loss_val = 0
            for t, content in loader_validation.items():

            # x is the features and y is the win rate
                x = content[0]
                y = content[1]

                x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
                y = y.to(device=device, dtype=torch.float)

                PER_C = model(x)
                F.sigmoid(PER_C)
                # Loss is the mean square error
                #logistic or not, l have not tried yet

                win_rate = sum(PER_C)
                loss_val += (y-win_rate)**2
            print('validation_loss:')
            loss_val /=4
            if e ==0:
                best_val_loss = loss_val[0].data

            if loss_val[0].data<= best_val_loss:

                best_val_loss = loss_val[0]
            else:
                
                break
            if e%20 == 0:
                his_val.append(loss_val[0].data)
                his_epoch.append(e)
                his_tra.append(loss_perepoch[0].data/25)
            print(loss_val[0])

        '''
        if e%100 == 0:
            torch.save(model, 'index_code1_linear.all')
        '''
        print(e,loss_perepoch/25)
    return his_epoch,his_tra,his_val
