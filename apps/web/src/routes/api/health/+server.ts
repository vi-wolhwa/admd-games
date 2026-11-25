import { json } from '@sveltejs/kit';

import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ locals }) => {
	const status = await locals.services.health.check();
	return json(status, { status: status.storage === 'ok' ? 200 : 503 });
};
