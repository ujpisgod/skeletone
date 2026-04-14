import ops
X_train=[[1,1],
         [1,0],
         [0,1],
         [0,0]]
Y_true= [[0.0],
         [1.0],
         [1.0],
         [0.0]]
W1 = ops.create_r_mat(2, 4)
B1 = ops.create_z_mat(1, 4)
W2 = ops.create_r_mat(4, 1)
B2 = ops.create_z_mat(1, 1)
Z1 = ops.mat_add(ops.mat_mul(X_train, W1), B1)
A1 = ops.relu(Z1)
Z2 = ops.mat_add(ops.mat_mul(A1, W2), B2)
Y_pred = ops.relu(Z2)
diff = ops.mat_sub(Y_true, Y_pred)
sum_squared_error = ops.mat_sum_sq(diff)
N, _ = ops.ismat(Y_true)
mse_loss = sum_squared_error/(2*N)
print(f"Final Prediction: {Y_pred}")
print(f"Initial Loss: {mse_loss}")