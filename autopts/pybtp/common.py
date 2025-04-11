from . import defs

CONTROLLER_INDEX = 0
CONTROLLER_INDEX_NONE = 0xff

mesh_btp = {
    "read_supp_cmds": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_READ_SUPPORTED_COMMANDS,
                       defs.BTP_INDEX_NONE, ""),
    "config_prov": (defs.BTP_SERVICE_ID_MESH,
                    defs.BTP_MESH_CMD_CONFIG_PROVISIONING,
                    CONTROLLER_INDEX),
    "prov_node": (defs.BTP_SERVICE_ID_MESH,
                  defs.BTP_MESH_CMD_PROVISION_NODE,
                  CONTROLLER_INDEX),
    "init": (defs.BTP_SERVICE_ID_MESH,
             defs.BTP_MESH_CMD_INIT,
             CONTROLLER_INDEX),
    "start": (defs.BTP_SERVICE_ID_MESH,
              defs.BTP_MESH_CMD_START,
              CONTROLLER_INDEX, ""),
    "reset": (defs.BTP_SERVICE_ID_MESH,
              defs.BTP_MESH_CMD_RESET,
              CONTROLLER_INDEX, ""),
    "input_num": (defs.BTP_SERVICE_ID_MESH,
                  defs.BTP_MESH_CMD_INPUT_NUMBER,
                  CONTROLLER_INDEX),
    "input_str": (defs.BTP_SERVICE_ID_MESH,
                  defs.BTP_MESH_CMD_INPUT_STRING,
                  CONTROLLER_INDEX),
    "iv_update_test_mode": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_IV_UPDATE_TEST_MODE,
                            CONTROLLER_INDEX),
    "iv_update_toggle": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_IV_UPDATE_TOGGLE,
                         CONTROLLER_INDEX, ""),
    "net_send": (defs.BTP_SERVICE_ID_MESH,
                 defs.BTP_MESH_CMD_NET_SEND,
                 CONTROLLER_INDEX),
    "health_generate_faults": (defs.BTP_SERVICE_ID_MESH,
                               defs.BTP_MESH_CMD_HEALTH_ADD_FAULTS,
                               CONTROLLER_INDEX, ""),
    "mesh_clear_faults": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_HEALTH_CLEAR_FAULTS,
                          CONTROLLER_INDEX, ""),
    "lpn": (defs.BTP_SERVICE_ID_MESH,
            defs.BTP_MESH_CMD_LPN_SET,
            CONTROLLER_INDEX),
    "lpn_poll": (defs.BTP_SERVICE_ID_MESH,
                 defs.BTP_MESH_CMD_LPN_POLL,
                 CONTROLLER_INDEX, ""),
    "model_send": (defs.BTP_SERVICE_ID_MESH,
                   defs.BTP_MESH_CMD_MODEL_SEND,
                   CONTROLLER_INDEX),
    "lpn_subscribe": (defs.BTP_SERVICE_ID_MESH,
                      defs.BTP_MESH_CMD_LPN_SUBSCRIBE,
                      CONTROLLER_INDEX),
    "lpn_unsubscribe": (defs.BTP_SERVICE_ID_MESH,
                        defs.BTP_MESH_CMD_LPN_UNSUBSCRIBE,
                        CONTROLLER_INDEX),
    "rpl_clear": (defs.BTP_SERVICE_ID_MESH,
                  defs.BTP_MESH_CMD_RPL_CLEAR,
                  CONTROLLER_INDEX, ""),
    "proxy_identity": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_PROXY_IDENTITY,
                       CONTROLLER_INDEX, ""),
    "composition_data_get": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_COMP_DATA_GET,
                             CONTROLLER_INDEX),
    "cfg_beacon_get": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_BEACON_GET,
                       CONTROLLER_INDEX),
    "cfg_beacon_set": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_BEACON_SET,
                       CONTROLLER_INDEX),
    "cfg_default_ttl_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_CFG_DEFAULT_TTL_GET,
                            CONTROLLER_INDEX),
    "cfg_default_ttl_set": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_CFG_DEFAULT_TTL_SET,
                            CONTROLLER_INDEX),
    "cfg_gatt_proxy_get": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_CFG_GATT_PROXY_GET,
                           CONTROLLER_INDEX),
    "cfg_gatt_proxy_set": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_CFG_GATT_PROXY_SET,
                           CONTROLLER_INDEX),
    "cfg_friend_get": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_FRIEND_GET,
                       CONTROLLER_INDEX),
    "cfg_friend_set": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_FRIEND_SET,
                       CONTROLLER_INDEX),
    "cfg_relay_get": (defs.BTP_SERVICE_ID_MESH,
                      defs.BTP_MESH_CMD_CFG_RELAY_GET,
                      CONTROLLER_INDEX),
    "cfg_relay_set": (defs.BTP_SERVICE_ID_MESH,
                      defs.BTP_MESH_CMD_CFG_RELAY_SET,
                      CONTROLLER_INDEX),
    "cfg_model_pub_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_PUB_GET,
                          CONTROLLER_INDEX),
    "cfg_model_pub_set": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_PUB_SET,
                          CONTROLLER_INDEX),
    "cfg_model_sub_add": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_SUB_ADD,
                          CONTROLLER_INDEX),
    "cfg_model_sub_del": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_SUB_DEL,
                          CONTROLLER_INDEX),
    "cfg_netkey_add": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_NETKEY_ADD,
                       CONTROLLER_INDEX),
    "cfg_netkey_get": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_NETKEY_GET,
                       CONTROLLER_INDEX),
    "cfg_netkey_del": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_NETKEY_DEL,
                       CONTROLLER_INDEX),
    "cfg_appkey_add": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_APPKEY_ADD,
                       CONTROLLER_INDEX),
    "cfg_appkey_del": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_APPKEY_DEL,
                       CONTROLLER_INDEX),
    "cfg_appkey_get": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_APPKEY_GET,
                       CONTROLLER_INDEX),
    "cfg_model_app_bind": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_CFG_MODEL_APP_BIND,
                           CONTROLLER_INDEX),
    "cfg_model_app_unbind": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_MODEL_APP_UNBIND,
                             CONTROLLER_INDEX),
    "cfg_model_app_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_APP_GET,
                          CONTROLLER_INDEX),
    "cfg_model_app_vnd_get": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_MODEL_APP_VND_GET,
                              CONTROLLER_INDEX),
    "cfg_heartbeat_pub_set": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_HEARTBEAT_PUB_SET,
                              CONTROLLER_INDEX),
    "cfg_heartbeat_pub_get": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_HEARTBEAT_PUB_GET,
                              CONTROLLER_INDEX),
    "cfg_heartbeat_sub_set": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_HEARTBEAT_SUB_SET,
                              CONTROLLER_INDEX),
    "cfg_heartbeat_sub_get": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_HEARTBEAT_SUB_GET,
                              CONTROLLER_INDEX),
    "cfg_net_transmit_get": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_NET_TRANSMIT_GET,
                             CONTROLLER_INDEX),
    "cfg_net_transmit_set": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_NET_TRANSMIT_SET,
                             CONTROLLER_INDEX),
    "cfg_model_sub_ovw": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_SUB_OVW,
                          CONTROLLER_INDEX),
    "cfg_model_sub_del_all": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_MODEL_SUB_DEL_ALL,
                              CONTROLLER_INDEX),
    "cfg_model_sub_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_MODEL_SUB_GET,
                          CONTROLLER_INDEX),
    "cfg_model_sub_vnd_get": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_CFG_MODEL_SUB_VND_GET,
                              CONTROLLER_INDEX),
    "cfg_model_sub_va_add": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_MODEL_SUB_VA_ADD,
                             CONTROLLER_INDEX),
    "cfg_model_sub_va_del": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_MODEL_SUB_VA_DEL,
                             CONTROLLER_INDEX),
    "cfg_model_sub_va_ovw": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_MODEL_SUB_VA_OVW,
                             CONTROLLER_INDEX),
    "cfg_netkey_update": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_NETKEY_UPDATE,
                          CONTROLLER_INDEX),
    "cfg_appkey_update": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_CFG_APPKEY_UPDATE,
                          CONTROLLER_INDEX),
    "cfg_node_idt_set": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_CFG_NODE_IDT_SET,
                         CONTROLLER_INDEX),
    "cfg_node_idt_get": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_CFG_NODE_IDT_GET,
                         CONTROLLER_INDEX),
    "cfg_node_reset": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_CFG_NODE_RESET,
                       CONTROLLER_INDEX),
    "cfg_lpn_polltimeout_get": (defs.BTP_SERVICE_ID_MESH,
                                defs.BTP_MESH_CMD_CFG_LPN_POLLTIMEOUT_GET,
                                CONTROLLER_INDEX),
    "cfg_model_pub_va_set": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_CFG_MODEL_PUB_VA_SET,
                             CONTROLLER_INDEX),
    "cfg_model_app_bind_vnd": (defs.BTP_SERVICE_ID_MESH,
                               defs.BTP_MESH_CMD_CFG_MODEL_APP_BIND_VND,
                               CONTROLLER_INDEX),
    "cfg_krp_get": (defs.BTP_SERVICE_ID_MESH,
                    defs.BTP_MESH_CMD_CFG_KRP_GET,
                    CONTROLLER_INDEX),
    "cfg_krp_set": (defs.BTP_SERVICE_ID_MESH,
                    defs.BTP_MESH_CMD_CFG_KRP_SET,
                    CONTROLLER_INDEX),
    "health_fault_get": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_HEALTH_FAULT_GET,
                         CONTROLLER_INDEX),
    "health_fault_clear": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_HEALTH_FAULT_CLEAR,
                           CONTROLLER_INDEX),
    "health_fault_test": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_HEALTH_FAULT_TEST,
                          CONTROLLER_INDEX),
    "health_period_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_HEALTH_PERIOD_GET,
                          CONTROLLER_INDEX),
    "health_period_set": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_HEALTH_PERIOD_SET,
                          CONTROLLER_INDEX),
    "health_attention_get": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_HEALTH_ATTENTION_GET,
                             CONTROLLER_INDEX),
    "health_attention_set": (defs.BTP_SERVICE_ID_MESH,
                             defs.BTP_MESH_CMD_HEALTH_ATTENTION_SET,
                             CONTROLLER_INDEX),
    "provision_adv": (defs.BTP_SERVICE_ID_MESH,
                      defs.BTP_MESH_CMD_PROVISION_ADV,
                      CONTROLLER_INDEX),
    "va_add": (defs.BTP_SERVICE_ID_MESH,
               defs.BTP_MESH_CMD_VA_ADD,
               CONTROLLER_INDEX),
    "va_del": (defs.BTP_SERVICE_ID_MESH,
               defs.BTP_MESH_CMD_VA_DEL,
               CONTROLLER_INDEX),
    "sar_transmitter_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_SAR_TRANSMITTER_GET,
                            CONTROLLER_INDEX),
    "sar_transmitter_set": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_SAR_TRANSMITTER_SET,
                            CONTROLLER_INDEX),
    "sar_receiver_get": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_SAR_RECEIVER_GET,
                         CONTROLLER_INDEX),
    "sar_receiver_set": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_SAR_RECEIVER_SET,
                         CONTROLLER_INDEX),
    "large_comp_data_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_LARGE_COMP_DATA_GET,
                            CONTROLLER_INDEX),
    "models_metadata_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_MODELS_METADATA_GET,
                            CONTROLLER_INDEX),
    "opcodes_aggregator_init": (defs.BTP_SERVICE_ID_MESH,
                                defs.BTP_MESH_CMD_OPCODES_AGGREGATOR_INIT,
                                CONTROLLER_INDEX),
    "opcodes_aggregator_send": (defs.BTP_SERVICE_ID_MESH,
                                defs.BTP_MESH_CMD_OPCODES_AGGREGATOR_SEND,
                                CONTROLLER_INDEX, ""),
    "comp_change_prepare": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_COMP_CHANGE_PREPARE,
                            CONTROLLER_INDEX),
    "rpr_scan_start": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_RPR_SCAN_START,
                       CONTROLLER_INDEX),
    "rpr_ext_scan_start": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_RPR_EXT_SCAN_START,
                           CONTROLLER_INDEX),
    "rpr_scan_caps_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_RPR_SCAN_CAPS_GET,
                          CONTROLLER_INDEX),
    "rpr_scan_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_RPR_SCAN_GET,
                          CONTROLLER_INDEX),
    "rpr_scan_stop": (defs.BTP_SERVICE_ID_MESH,
                      defs.BTP_MESH_CMD_RPR_SCAN_STOP,
                      CONTROLLER_INDEX),
    "rpr_link_get": (defs.BTP_SERVICE_ID_MESH,
                     defs.BTP_MESH_CMD_RPR_LINK_GET,
                     CONTROLLER_INDEX),
    "rpr_link_close": (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_RPR_LINK_CLOSE,
                       CONTROLLER_INDEX),
    "rpr_prov_remote": (defs.BTP_SERVICE_ID_MESH,
                        defs.BTP_MESH_CMD_RPR_PROV_REMOTE,
                        CONTROLLER_INDEX),
    "rpr_reprov_remote": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_RPR_REPROV_REMOTE,
                          CONTROLLER_INDEX),
    "priv_beacon_get": (defs.BTP_SERVICE_ID_MESH,
                        defs.BTP_MESH_CMD_PRIV_BEACON_GET,
                        CONTROLLER_INDEX),
    "priv_beacon_set": (defs.BTP_SERVICE_ID_MESH,
                        defs.BTP_MESH_CMD_PRIV_BEACON_SET,
                        CONTROLLER_INDEX),
    "priv_gatt_proxy_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_PRIV_GATT_PROXY_GET,
                            CONTROLLER_INDEX),
    "priv_gatt_proxy_set": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_PRIV_GATT_PROXY_SET,
                            CONTROLLER_INDEX),
    "priv_node_id_get": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_PRIV_NODE_ID_GET,
                         CONTROLLER_INDEX),
    "priv_node_id_set": (defs.BTP_SERVICE_ID_MESH,
                         defs.BTP_MESH_CMD_PRIV_NODE_ID_SET,
                         CONTROLLER_INDEX),
    "proxy_private_identity": (defs.BTP_SERVICE_ID_MESH,
                               defs.BTP_MESH_CMD_PROXY_PRIVATE_IDENTITY,
                               CONTROLLER_INDEX),
    "subnet_bridge_get": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_SUBNET_BRIDGE_GET,
                          CONTROLLER_INDEX),
    "subnet_bridge_set": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_SUBNET_BRIDGE_SET,
                          CONTROLLER_INDEX),
    "bridging_table_add": (defs.BTP_SERVICE_ID_MESH,
                          defs.BTP_MESH_CMD_BRIDGING_TABLE_ADD,
                          CONTROLLER_INDEX),
    "bridging_table_remove": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_BRIDGING_TABLE_REMOVE,
                              CONTROLLER_INDEX),
    "bridged_subnets_get": (defs.BTP_SERVICE_ID_MESH,
                            defs.BTP_MESH_CMD_BRIDGED_SUBNETS_GET,
                            CONTROLLER_INDEX),
    "bridging_table_get": (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_BRIDGING_TABLE_GET,
                           CONTROLLER_INDEX),
    "bridge_capability_get": (defs.BTP_SERVICE_ID_MESH,
                              defs.BTP_MESH_CMD_BRIDGE_CAPABILITY_GET,
                              CONTROLLER_INDEX),
    "od_priv_proxy_get":  (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_OD_PRIV_PROXY_GET,
                           CONTROLLER_INDEX),
    "od_priv_proxy_set":  (defs.BTP_SERVICE_ID_MESH,
                           defs.BTP_MESH_CMD_OD_PRIV_PROXY_SET,
                           CONTROLLER_INDEX),
    "srpl_clear":  (defs.BTP_SERVICE_ID_MESH,
                    defs.BTP_MESH_CMD_SRPL_CLEAR,
                    CONTROLLER_INDEX),
    "proxy_solicit":  (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_PROXY_SOLICIT,
                       CONTROLLER_INDEX),
    "proxy_connect":  (defs.BTP_SERVICE_ID_MESH,
                       defs.BTP_MESH_CMD_PROXY_CONNECT,
                       CONTROLLER_INDEX),
}


gatt_cl = {
    "read_supp_cmds": (defs.BTP_SERVICE_ID_GATTC,
                       defs.BTP_GATTC_CMD_READ_SUPPORTED_COMMANDS,
                       defs.BTP_INDEX_NONE, ""),
    "exchange_mtu": (defs.BTP_SERVICE_ID_GATTC,
                     defs.BTP_GATTC_CMD_EXCHANGE_MTU,
                     CONTROLLER_INDEX),
    "disc_all_prim": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_DISC_ALL_PRIM,
                      CONTROLLER_INDEX),
    "disc_prim_uuid": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_DISC_PRIM_UUID,
                       CONTROLLER_INDEX),
    "find_included": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_FIND_INCLUDED,
                      CONTROLLER_INDEX),
    "disc_all_chrc": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_DISC_ALL_CHRC,
                      CONTROLLER_INDEX),
    "disc_chrc_uuid": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_DISC_CHRC_UUID,
                       CONTROLLER_INDEX),
    "disc_all_desc": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_DISC_ALL_DESC,
                      CONTROLLER_INDEX),
    "read": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_READ, CONTROLLER_INDEX),
    "read_uuid": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_READ_UUID,
                  CONTROLLER_INDEX),
    "read_long": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_READ_LONG,
                  CONTROLLER_INDEX),
    "read_multiple": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_READ_MULTIPLE,
                      CONTROLLER_INDEX),
    "write_without_rsp": (defs.BTP_SERVICE_ID_GATTC,
                          defs.BTP_GATTC_CMD_WRITE_WITHOUT_RSP, CONTROLLER_INDEX),
    "signed_write": (defs.BTP_SERVICE_ID_GATTC,
                     defs.BTP_GATTC_CMD_SIGNED_WRITE_WITHOUT_RSP, CONTROLLER_INDEX),
    "write": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_WRITE, CONTROLLER_INDEX),
    "write_long": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_WRITE_LONG,
                   CONTROLLER_INDEX),
    "write_reliable": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_WRITE_RELIABLE,
                       CONTROLLER_INDEX),
    "cfg_notify": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_CFG_NOTIFY,
                   CONTROLLER_INDEX),
    "cfg_indicate": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_CFG_INDICATE,
                     CONTROLLER_INDEX),
    "read_multiple_var": (defs.BTP_SERVICE_ID_GATTC, defs.BTP_GATTC_CMD_READ_MULTIPLE_VAR,
                          CONTROLLER_INDEX),
}


cap_btp = {
    'read_supported_cmds': (defs.BTP_SERVICE_ID_CAP,
                            defs.BTP_CAP_CMD_READ_SUPPORTED_COMMANDS,
                            CONTROLLER_INDEX),
    'discover': (defs.BTP_SERVICE_ID_CAP, defs.BTP_CAP_CMD_DISCOVER, CONTROLLER_INDEX),
    'unicast_setup_ase': (defs.BTP_SERVICE_ID_CAP, defs.BTP_CAP_CMD_UNICAST_SETUP_ASE, CONTROLLER_INDEX),
    'unicast_audio_start': (defs.BTP_SERVICE_ID_CAP, defs.BTP_CAP_CMD_UNICAST_AUDIO_START, CONTROLLER_INDEX),
    'unicast_audio_update': (defs.BTP_SERVICE_ID_CAP, defs.BTP_CAP_CMD_UNICAST_AUDIO_UPDATE, CONTROLLER_INDEX),
    'unicast_audio_stop': (defs.BTP_SERVICE_ID_CAP, defs.BTP_CAP_CMD_UNICAST_AUDIO_STOP, CONTROLLER_INDEX),
    'broadcast_source_setup_stream': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_SETUP_STREAM, CONTROLLER_INDEX),
    'broadcast_source_setup_subgroup': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_SETUP_SUBGROUP, CONTROLLER_INDEX),
    'broadcast_source_setup': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_SETUP, CONTROLLER_INDEX),
    'broadcast_source_release': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_RELEASE, CONTROLLER_INDEX),
    'broadcast_adv_start': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_ADV_START, CONTROLLER_INDEX),
    'broadcast_adv_stop': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_ADV_STOP, CONTROLLER_INDEX),
    'broadcast_source_start': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_START, CONTROLLER_INDEX),
    'broadcast_source_stop': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_STOP, CONTROLLER_INDEX),
    'broadcast_source_update': (defs.BTP_SERVICE_ID_CAP,
        defs.BTP_CAP_CMD_BROADCAST_SOURCE_UPDATE, CONTROLLER_INDEX),
}


aics_btp = {
    "read_supported_cmds": (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_READ_SUPPORTED_COMMANDS,
                            CONTROLLER_INDEX, ""),
    "set_gain":            (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_SET_GAIN,
                            CONTROLLER_INDEX),
    "mute":                (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_MUTE,
                            CONTROLLER_INDEX),
    "unmute":              (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_UNMUTE,
                            CONTROLLER_INDEX),
    "auto_gain":           (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_AUTO_GAIN_SET,
                            CONTROLLER_INDEX),
    "man_gain":            (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_MAN_GAIN_SET,
                            CONTROLLER_INDEX),
    "man_gain_only":       (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_SET_MAN_GAIN_ONLY,
                            CONTROLLER_INDEX, ""),
    "auto_gain_only":      (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_SET_AUTO_GAIN_ONLY,
                            CONTROLLER_INDEX, ""),
    "desc_set":            (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_AUDIO_DESC_SET,
                            CONTROLLER_INDEX),
    "mute_disable":        (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_MUTE_DISABLE,
                            CONTROLLER_INDEX, ""),
    "aics_state":          (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_STATE_GET,
                            CONTROLLER_INDEX),
    "status":              (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_STATUS_GET,
                            CONTROLLER_INDEX),
    "type":                (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_TYPE_GET,
                            CONTROLLER_INDEX),
    "gain_setting_prop":   (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_GAIN_SETTING_PROP_GET,
                            CONTROLLER_INDEX),
    "description":         (defs.BTP_SERVICE_ID_AICS,
                            defs.BTP_AICS_CMD_DESCRIPTION_GET,
                            CONTROLLER_INDEX)
}
supported_svcs_cmds = {
    "CORE": {
        "service": 1 << defs.BTP_SERVICE_ID_CORE,
        "supported_commands": defs.BTP_CORE_CMD_READ_SUPPORTED_COMMANDS
    },
    "GAP": {
        "service": 1 << defs.BTP_SERVICE_ID_GAP,
        "supported_commands": defs.BTP_GAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "GATT": {
        "service": 1 << defs.BTP_SERVICE_ID_GATT,
        "supported_commands": defs.BTP_GATT_CMD_READ_SUPPORTED_COMMANDS
    },
    "L2CAP": {
        "service": 1 << defs.BTP_SERVICE_ID_L2CAP,
        "supported_commands": defs.BTP_L2CAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "MESH": {
        "service": 1 << defs.BTP_SERVICE_ID_MESH,
        "supported_commands": defs.BTP_MESH_CMD_READ_SUPPORTED_COMMANDS
    },
    "MESH_MMDL": {
        "service": 1 << defs.BTP_SERVICE_ID_MMDL,
        "supported_commands": defs.BTP_MMDL_CMD_READ_SUPPORTED_COMMANDS
    },
    "GATT_CL": {
        "service": 1 << defs.BTP_SERVICE_ID_GATTC,
        "supported_commands": defs.BTP_GATTC_CMD_READ_SUPPORTED_COMMANDS
    },
    "VCS": {
        "service": 1 << defs.BTP_SERVICE_ID_VCS,
        "supported_commands": defs.BTP_VCS_CMD_READ_SUPPORTED_COMMANDS
    },
    "IAS": {
        "service": 1 << defs.BTP_SERVICE_ID_IAS
    },
    "AICS": {
        "service": 1 << defs.BTP_SERVICE_ID_AICS,
        "supported_commands": defs.BTP_AICS_CMD_READ_SUPPORTED_COMMANDS
    },
    "VOCS": {
        "service": 1 << defs.BTP_SERVICE_ID_VOCS,
        "supported_commands": defs.BTP_VOCS_CMD_READ_SUPPORTED_COMMANDS
    },
    "PACS": {
        "service": 1 << defs.BTP_SERVICE_ID_PACS,
        "supported_commands": defs.BTP_PACS_CMD_READ_SUPPORTED_COMMANDS
    },
    "ASCS": {
        "service": 1 << defs.BTP_SERVICE_ID_ASCS,
        "supported_commands": defs.BTP_ASCS_CMD_READ_SUPPORTED_COMMANDS
    },
    "BAP": {
        "service": 1 << defs.BTP_SERVICE_ID_BAP,
        "supported_commands": defs.BTP_BAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "MICP": {
        "service": 1 << defs.BTP_SERVICE_ID_MICP,
        "supported_commands": defs.BTP_MICP_CMD_READ_SUPPORTED_COMMANDS
    },
    "HAS": {
        "service": 1 << defs.BTP_SERVICE_ID_HAS,
        "supported_commands": defs.BTP_HAS_CMD_READ_SUPPORTED_COMMANDS
    },
    "CSIS": {
        "service": 1 << defs.BTP_SERVICE_ID_CSIS,
        "supported_commands": defs.BTP_CSIS_CMD_READ_SUPPORTED_COMMANDS
    },
    "MICS": {
        "service": 1 << defs.BTP_SERVICE_ID_MICS,
        "supported_commands": defs.BTP_MICS_CMD_READ_SUPPORTED_COMMANDS
    },
    "CCP": {
        "service": 1 << defs.BTP_SERVICE_ID_CCP,
        "supported_commands": defs.BTP_CCP_CMD_READ_SUPPORTED_COMMANDS
    },
    "VCP": {
        "service": 1 << defs.BTP_SERVICE_ID_VCP,
        "supported_commands": defs.BTP_VCP_CMD_READ_SUPPORTED_COMMANDS
    },
    "MCP": {
        "service": 1 << defs.BTP_SERVICE_ID_MCP,
        "supported_commands": defs.BTP_MCP_CMD_READ_SUPPORTED_COMMANDS
    },
    "GMCS": {
        "service": 1 << defs.BTP_SERVICE_ID_GMCS,
        "supported_commands": defs.BTP_GMCS_CMD_READ_SUPPORTED_COMMANDS
    },
    "HAP": {
        "service": 1 << defs.BTP_SERVICE_ID_HAP,
        "supported_commands": defs.BTP_HAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "CAP": {
        "service": 1 << defs.BTP_SERVICE_ID_CAP,
        "supported_commands": defs.BTP_CAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "CSIP": {
        "service": 1 << defs.BTP_SERVICE_ID_CSIP,
        "supported_commands": defs.BTP_CSIP_CMD_READ_SUPPORTED_COMMANDS
    },
    "TBS": {
        "service": 1 << defs.BTP_SERVICE_ID_TBS,
        "supported_commands": defs.BTP_TBS_CMD_READ_SUPPORTED_COMMANDS
    },
    "TMAP": {
        "service": 1 << defs.BTP_SERVICE_ID_TMAP,
        "supported_commands": defs.BTP_TMAP_CMD_READ_SUPPORTED_COMMANDS
    },
    "OTS": {
        "service": 1 << defs.BTP_SERVICE_ID_OTS,
        "supported_commands": defs.BTP_OTS_CMD_READ_SUPPORTED_COMMANDS
    },
    "PBP": {
        "service": 1 << defs.BTP_SERVICE_ID_PBP,
        "supported_commands": defs.BTP_PBP_CMD_READ_SUPPORTED_COMMANDS
    },
    "CAS": {
        "supported_commands": defs.BTP_CAS_CMD_READ_SUPPORTED_COMMANDS
    },
    "BASS": {
        "supported_commands": defs.BTP_BASS_CMD_READ_SUPPORTED_COMMANDS
    },
    # GENERATOR append 1
}

reg_unreg_service = {
    "gap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GAP),
    "gap_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                  defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GAP),
    "gatt_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GATT),
    "gatt_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                   defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GATT),
    "l2cap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                  defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_L2CAP),
    "l2cap_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                    defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_L2CAP),
    "mesh_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MESH),
    "mesh_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                   defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MESH),
    "mmdl_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MMDL),
    "mmdl_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                   defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MMDL),
    "gatt_cl_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                    defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GATTC),
    "gatt_cl_unreg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_UNREGISTER_SERVICE,
                      defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GATTC),
    "vcs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_VCS),
    "vocs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_VOCS),
    "aics_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_AICS),
    "ias_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_IAS),
    "pacs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_PACS),
    "ascs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_ASCS),
    "bap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_BAP),
    "has_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_HAS),
    "csis_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_CSIS),
    "micp_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MICP),
    "mics_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MICS),
    "ccp_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_CCP),
    "vcp_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_VCP),
    "cas_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_CAS),
    "mcp_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_MCP),
    "gmcs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_GMCS),
    "hap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_HAP),
    "cap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_CAP),
    "csip_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_CSIP),
    "tbs_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_TBS),
    "tmap_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                 defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_TMAP),
    "ots_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_OTS),
    "pbp_reg": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_REGISTER_SERVICE,
                defs.BTP_INDEX_NONE, defs.BTP_SERVICE_ID_PBP),
    # GENERATOR append 2
    "read_supp_cmds": (defs.BTP_SERVICE_ID_CORE,
                       defs.BTP_CORE_CMD_READ_SUPPORTED_COMMANDS,
                       defs.BTP_INDEX_NONE, ""),
    "read_supp_svcs": (defs.BTP_SERVICE_ID_CORE,
                       defs.BTP_CORE_CMD_READ_SUPPORTED_SERVICES,
                       defs.BTP_INDEX_NONE, ""),
    "log_message": (defs.BTP_SERVICE_ID_CORE, defs.BTP_CORE_CMD_LOG_MESSAGE,
                    defs.BTP_INDEX_NONE),
}
