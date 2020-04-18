CREATE TABLE `chain_data`.`first_round_staking`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'user address',
  `amount` decimal(65, 10) NOT NULL COMMENT 'incentive amount',
  `staking_amount` bigint(65) NOT NULL COMMENT 'staking amount',
  `epoch` int(255) NULL DEFAULT NULL COMMENT 'epoch',
  `peerpubkey` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT 'pubkey',
  `incentive_month` date NOT NULL COMMENT 'incentive calculation month',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14833 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;
