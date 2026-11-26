CREATE TABLE `game_media` (
	`id` text PRIMARY KEY NOT NULL,
	`game_id` text NOT NULL,
	`kind` text NOT NULL,
	`url` text NOT NULL,
	`position` integer NOT NULL,
	FOREIGN KEY (`game_id`) REFERENCES `games`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `game_media_by_game` ON `game_media` (`game_id`,`position`);--> statement-breakpoint
CREATE TABLE `game_tags` (
	`game_id` text NOT NULL,
	`tag_id` text NOT NULL,
	`position` integer NOT NULL,
	PRIMARY KEY(`game_id`, `tag_id`),
	FOREIGN KEY (`game_id`) REFERENCES `games`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`tag_id`) REFERENCES `tags`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `game_tags_by_tag` ON `game_tags` (`tag_id`,`game_id`);--> statement-breakpoint
CREATE TABLE `games` (
	`id` text PRIMARY KEY NOT NULL,
	`slug` text NOT NULL,
	`maker_id` text NOT NULL,
	`status` text NOT NULL,
	`title` text NOT NULL,
	`summary` text NOT NULL,
	`launch` text NOT NULL,
	`length` integer NOT NULL,
	`phone` integer NOT NULL,
	`players_min` integer NOT NULL,
	`players_max` integer NOT NULL,
	`scan_passed` integer NOT NULL,
	`cover_url` text NOT NULL,
	`published_at` integer,
	`recommend_count` integer DEFAULT 0 NOT NULL,
	`review_count` integer DEFAULT 0 NOT NULL,
	`created_at` integer NOT NULL,
	FOREIGN KEY (`maker_id`) REFERENCES `makers`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE UNIQUE INDEX `games_slug_unique` ON `games` (`slug`);--> statement-breakpoint
CREATE INDEX `games_by_recommended` ON `games` (`status`,`recommend_count`,`id`);--> statement-breakpoint
CREATE INDEX `games_by_new` ON `games` (`status`,`published_at`,`id`);--> statement-breakpoint
CREATE INDEX `games_by_short` ON `games` (`status`,`length`,`recommend_count`,`id`);--> statement-breakpoint
CREATE TABLE `makers` (
	`id` text PRIMARY KEY NOT NULL,
	`slug` text NOT NULL,
	`name` text NOT NULL,
	`created_at` integer NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `makers_slug_unique` ON `makers` (`slug`);--> statement-breakpoint
CREATE TABLE `tags` (
	`id` text PRIMARY KEY NOT NULL,
	`slug` text NOT NULL,
	`name` text NOT NULL,
	`alias_of` text,
	`game_count` integer DEFAULT 0 NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `tags_slug_unique` ON `tags` (`slug`);