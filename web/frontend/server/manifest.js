const manifest = {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png"]),
	mimeTypes: {".png":"image/png"},
	_: {
		entry: {"file":"_app/immutable/start-0d59a454.js","imports":["_app/immutable/start-0d59a454.js","_app/immutable/chunks/index-83f7c07d.js","_app/immutable/chunks/singletons-73b30961.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			() => import('./chunks/0-b0afddf8.js'),
			() => import('./chunks/1-314b1bd4.js'),
			() => import('./chunks/2-84fed858.js')
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0], errors: [1], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
};

export { manifest };
//# sourceMappingURL=manifest.js.map
