def train(model,loader_train, device,optimizer, dtype,epochs,print_process=True):
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
    model = model.to(device=device)  # move the model parameters to CPU/GPU
    for e in range(epochs):
        time = 0
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


            win_rate = sum(PER_C)
            criterion =nn.MSELoss()

            loss = criterion(win_rate, y)

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
            time+=1

            if print_process==True:
                print('now we have')
                print(t,win_rate,y)
        # every ten epochs print the loss on validation set
        '''
        if e%10 == 0:
            for t, content in loader_validation.items():

            # x is the features and y is the win rate
                x = content[0]
                y = content[1]

                x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
                y = y.to(device=device, dtype=torch.float)

                PER_C = model(x)
                # Loss is the mean square error
                #logistic or not, l have not tried yet


                win_rate = sum(PER_C)
                criterion =nn.MSELoss()

                loss = criterion(win_rate, y)
        
        if e%100 == 0:
            torch.save(model, 'index_code1_linear.all')
        '''
        print(e)
