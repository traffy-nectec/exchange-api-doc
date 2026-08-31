class TraffyExchangeClient {
  constructor(baseUrl = "https://publicapi.traffy.in.th/exchange-api") {
    this.baseUrl = baseUrl;
    this.token = null;
  }

  async authenticate(username, password) {
    const res = await fetch(`${this.baseUrl}/get-auth/v1`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user: username, pass: password })
    });
    const data = await res.json();
    if (data.status === "success" && data.results && data.results.length > 0) {
      this.token = data.results[0].token;
    }
    return data;
  }

  getHeaders() {
    if (!this.token) {
      throw new Error("Client not authenticated. Call authenticate() first.");
    }
    return {
      "Authorization": `Bearer ${this.token}`,
      "Content-Type": "application/json"
    };
  }

  async getIssues(params = {}) {
    const res = await fetch(`${this.baseUrl}/get-issues/v1`, {
      method: "POST",
      headers: this.getHeaders(),
      body: JSON.stringify(params)
    });
    return res.json();
  }

  async newIssue(payload) {
    const res = await fetch(`${this.baseUrl}/new-issue/v1`, {
      method: "POST",
      headers: this.getHeaders(),
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async updateIssue(payload) {
    const res = await fetch(`${this.baseUrl}/update-issue/v1`, {
      method: "POST",
      headers: this.getHeaders(),
      body: JSON.stringify(payload)
    });
    return res.json();
  }
}

module.exports = TraffyExchangeClient;
