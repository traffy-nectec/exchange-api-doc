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

  // params: { org_id, duration ("today" | "all") } — all optional query string params
  async getIssues(params = {}) {
    const query = new URLSearchParams(params).toString();
    const res = await fetch(`${this.baseUrl}/get-issues/v1${query ? `?${query}` : ""}`, {
      method: "GET",
      headers: this.getHeaders()
    });
    return res.json();
  }

  // ticket_id is REQUIRED — get-issue/v1 does not support client_ticket_id
  async getIssue(ticketId, params = {}) {
    const query = new URLSearchParams({ ticket_id: ticketId, ...params }).toString();
    const res = await fetch(`${this.baseUrl}/get-issue/v1?${query}`, {
      method: "GET",
      headers: this.getHeaders()
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

  // payload: { ticket_id | client_ticket_id | message_id, note, ... one of
  //   issue_status_id | org_status_id | state_name | status_id/state_id/org_state_id (legacy) }
  async updateIssue(payload) {
    const res = await fetch(`${this.baseUrl}/update-issue/v1`, {
      method: "PATCH",
      headers: this.getHeaders(),
      body: JSON.stringify(payload)
    });
    return res.json();
  }
}

module.exports = TraffyExchangeClient;
