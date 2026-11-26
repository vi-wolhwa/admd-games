import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ locals }) => {
	const status = await locals.services.health.check();
	return Response.json(status, { status: status.storage === 'ok' ? 200 : 503 });
};
