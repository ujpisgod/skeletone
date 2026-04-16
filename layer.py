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
for epoch in range(10000):
    # --- 순전파 (Forward) ---
    Y1 = ops.mat_add(ops.mat_mul(X_train, W1), B1)
    L1 = ops.relu(Y1)
    L2 = ops.mat_add(ops.mat_mul(L1, W2), B2)
    Y_pred = ops.relu(L2)

    # --- 오차 계산 ---
    # 그라디언트 공식에 맞게 예측값에서 실제값을 뺍니다.
    diff = ops.mat_sub(Y_pred, Y_true)
    sum_squared_error = ops.mat_sum_sq(diff)
    N, _ = ops.ismat(Y_true)
    mse_loss = sum_squared_error / (2 * N)

    # --- 역전파 (Backward) ---
    dY_pred = ops.mat_mul_scalar(diff, 1 / N)
    dL2 = ops.relu_backward(dY_pred, L2)
    dW2 = ops.mat_mul(ops.tran(L1), dL2)
    dB2 = ops.mat_sum_axis0(dL2)

    dA1 = ops.mat_mul(dL2, ops.tran(W2))
    dL1 = ops.relu_backward(dA1, Y1)
    dW1 = ops.mat_mul(ops.tran(X_train), dL1)
    dB1 = ops.mat_sum_axis0(dL1)

    # --- 업데이트 (Update) ---
    lr = 0.1
    W2 = ops.mat_sub(W2, ops.mat_mul_scalar(dW2, lr))
    B2 = ops.mat_sub(B2, ops.mat_mul_scalar(dB2, lr))
    W1 = ops.mat_sub(W1, ops.mat_mul_scalar(dW1, lr))
    B1 = ops.mat_sub(B1, ops.mat_mul_scalar(dB1, lr))

    # 1000번마다 진행 상황 출력
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {mse_loss:.6f}")

print("\n--- 학습 완료 ---")
print(f"최종 예측값: {Y_pred}")