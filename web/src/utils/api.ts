async function baseAPi(url: string, options: RequestInit) {
  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}${url}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    return await response.json();
  }
  if (response.status >= 400 && response.status < 500) {
    const data = await response.json();
    if (data.detail) {
      throw new Error(data.detail);
    }
    throw new Error("Request failed with status code: " + response.status);
  }
  throw new Error("Network response was not ok.");
}

export const api = {
  get: (url: string) => baseAPi(url, { method: "GET" }),
  post: <T>(url: string, body: T) =>
    baseAPi(url, { method: "POST", ...(body && { body: JSON.stringify(body) }) }),
  patch: <T>(url: string, body: T) =>
    baseAPi(url, { method: "PATCH", ...(body && { body: JSON.stringify(body) }) }),
};
