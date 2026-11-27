CREATE TABLE `replies` (
	`id` text PRIMARY KEY NOT NULL,
	`review_id` text NOT NULL,
	`author_id` text NOT NULL,
	`body` text NOT NULL,
	`created_at` integer NOT NULL,
	`updated_at` integer,
	FOREIGN KEY (`review_id`) REFERENCES `reviews`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`author_id`) REFERENCES `profiles`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `replies_by_review` ON `replies` (`review_id`,`created_at`,`id`);--> statement-breakpoint
ALTER TABLE `makers` ADD `profile_id` text;--> statement-breakpoint
CREATE UNIQUE INDEX `profiles_display_name_unique` ON `profiles` (`display_name`);