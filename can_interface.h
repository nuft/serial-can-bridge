#ifndef CAN_INTERFACE_H
#define CAN_INTERFACE_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

void can_interface_send(bool ext, uint32_t id, void *data, uint8_t len);

void can_interface_receive(bool *ext, uint32_t *id, void *data, uint8_t *len);

#ifdef __cplusplus
}
#endif

#endif // CAN_INTERFACE_H
