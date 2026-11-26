DROP INDEX `games_by_short`;--> statement-breakpoint
ALTER TABLE `games` ADD `play_count` integer DEFAULT 0 NOT NULL;--> statement-breakpoint
CREATE INDEX `games_by_played` ON `games` (`status`,`play_count`,`recommend_count`,`id`);--> statement-breakpoint
CREATE INDEX `games_by_reviews` ON `games` (`status`,`review_count`,`id`);