ALTER TABLE `games` ADD `version` text;--> statement-breakpoint
CREATE UNIQUE INDEX `reviews_one_per_version` ON `reviews` (`game_id`,`author_id`,`version`);