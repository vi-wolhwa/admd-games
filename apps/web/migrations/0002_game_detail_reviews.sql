CREATE TABLE `profiles` (
	`id` text PRIMARY KEY NOT NULL,
	`display_name` text NOT NULL,
	`face_char` text NOT NULL,
	`face_color` text NOT NULL,
	`review_count` integer DEFAULT 0 NOT NULL,
	`created_at` integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE `recommendations` (
	`game_id` text NOT NULL,
	`user_id` text NOT NULL,
	`created_at` integer NOT NULL,
	PRIMARY KEY(`game_id`, `user_id`),
	FOREIGN KEY (`game_id`) REFERENCES `games`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`user_id`) REFERENCES `profiles`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE TABLE `review_phrases` (
	`review_id` text NOT NULL,
	`phrase` text NOT NULL,
	`position` integer NOT NULL,
	PRIMARY KEY(`review_id`, `phrase`),
	FOREIGN KEY (`review_id`) REFERENCES `reviews`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `review_phrases_by_phrase` ON `review_phrases` (`phrase`,`review_id`);--> statement-breakpoint
CREATE TABLE `review_replies` (
	`review_id` text PRIMARY KEY NOT NULL,
	`body` text NOT NULL,
	`note` text,
	`created_at` integer NOT NULL,
	FOREIGN KEY (`review_id`) REFERENCES `reviews`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE TABLE `reviews` (
	`id` text PRIMARY KEY NOT NULL,
	`game_id` text NOT NULL,
	`author_id` text NOT NULL,
	`body` text NOT NULL,
	`play_minutes` integer,
	`version` text,
	`helpful_count` integer DEFAULT 0 NOT NULL,
	`created_at` integer NOT NULL,
	FOREIGN KEY (`game_id`) REFERENCES `games`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`author_id`) REFERENCES `profiles`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `reviews_by_helpful` ON `reviews` (`game_id`,`helpful_count`,`created_at`,`id`);--> statement-breakpoint
CREATE INDEX `reviews_by_recent` ON `reviews` (`game_id`,`created_at`,`id`);--> statement-breakpoint
CREATE INDEX `reviews_by_played` ON `reviews` (`game_id`,`play_minutes`,`created_at`,`id`);--> statement-breakpoint
ALTER TABLE `games` ADD `description` text DEFAULT '' NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `pc` integer DEFAULT true NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `pad` integer DEFAULT false NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `controls` text DEFAULT '' NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `languages` text DEFAULT '' NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `cautions` text DEFAULT '' NOT NULL;--> statement-breakpoint
ALTER TABLE `games` ADD `min_spec` text;