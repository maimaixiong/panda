int cangw_rx_hook(CAN_FIFOMailBox_TypeDef *to_push) {
  UNUSED(to_push);
  return true;
}

static int cangw_fwd_hook(int bus_num, CAN_FIFOMailBox_TypeDef *to_fwd) {
  UNUSED(bus_num);
  UNUSED(to_fwd);
  return -1;
}


static void cangw_init(int16_t param) {
  UNUSED(param);
  controls_allowed = true;
  relay_malfunction_reset();
}

static int cangw_tx_hook(CAN_FIFOMailBox_TypeDef *to_send) {
  UNUSED(to_send);
  return true;
}

static int cangw_tx_lin_hook(int lin_num, uint8_t *data, int len) {
  UNUSED(lin_num);
  UNUSED(data);
  UNUSED(len);
  return true;
}

const safety_hooks cangw_hooks = {
  .init = cangw_init,
  .rx = cangw_rx_hook,
  .tx = cangw_tx_hook,
  .tx_lin = cangw_tx_lin_hook,
  .fwd = cangw_fwd_hook,
};
