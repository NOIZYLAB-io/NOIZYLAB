# Tailscale Configuration Templates

This directory contains configuration templates for setting up Tailscale with NOIZYLAB-specific policies.

## ACL Template

**File**: `tailscale-acl-template.json`

This template provides a pre-configured Access Control List (ACL) for NOIZYLAB infrastructure.

### Features

- **Tag-based Access Control**: Organized by roles (servers, dev, prod, database, api)
- **Tailscale SSH**: Configured SSH access for admins and developers
- **Subnet Routing**: Auto-approval rules for network routes
- **Exit Nodes**: Auto-approval for designated servers
- **Database Access**: Granular access control for database ports

### Usage

1. **Copy the template**:
   ```bash
   cp config/tailscale-acl-template.json /tmp/noizylab-acl.json
   ```

2. **Customize for your network**:
   - Replace example subnet ranges (192.0.2.0/24, 198.51.100.0/24) with your actual network CIDRs
   - Adjust tag names if needed
   - Add or remove access rules based on your requirements

3. **Apply to your Tailscale network**:
   - Visit https://login.tailscale.com/admin/acls
   - Click "Edit ACLs"
   - Paste your customized configuration
   - Click "Save"

4. **Test your ACLs**:
   The template includes test cases. Run them in the admin console to verify connectivity.

### Tag Definitions

- **tag:noizylab-servers**: General purpose servers
- **tag:noizylab-dev**: Development machines
- **tag:noizylab-prod**: Production servers
- **tag:noizylab-database**: Database servers
- **tag:noizylab-api**: API servers

### Security Model

The template implements a zero-trust security model:

1. **Default Deny**: Only explicitly allowed connections are permitted
2. **Least Privilege**: Users and services have minimum required access
3. **Role-Based Access**: Access is granted based on device tags
4. **Admin Override**: Admins have full access for emergency situations

### SSH Configuration

Tailscale SSH is configured with:
- Admins can SSH as any user including root
- Developers can SSH to servers as non-root users
- No SSH key management required

### Auto-Approvers

The template configures automatic approval for:
- Subnet routes from tagged servers
- Exit node advertisements from tagged servers

This reduces manual approval overhead while maintaining security.

### Network Segments

The ACL defines these logical network segments:

```
┌─────────────────┐
│   Admins        │──────> Full Access
└─────────────────┘

┌─────────────────┐     ┌──────────────────┐
│   Dev Machines  │────>│   Servers        │
└─────────────────┘     └──────────────────┘

┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   API Servers   │────>│   Database       │<────│   Dev Machines   │
└─────────────────┘     └──────────────────┘     └──────────────────┘
                               (Ports 5432, 3306)

┌─────────────────┐     ┌──────────────────┐
│   Prod Servers  │────>│   API Servers    │
└─────────────────┘     └──────────────────┘
                               (Ports 80, 443)
```

### Customization Examples

#### Add a new tag:

```json
"tagOwners": {
  "tag:noizylab-monitoring": ["autogroup:admin"]
}
```

#### Allow monitoring access to all servers:

```json
{
  "action": "accept",
  "src": ["tag:noizylab-monitoring"],
  "dst": ["tag:noizylab-servers:9090", "tag:noizylab-servers:9100"],
  "comment": "Monitoring can access Prometheus and node_exporter"
}
```

#### Add specific port access:

```json
{
  "action": "accept",
  "src": ["tag:noizylab-dev"],
  "dst": ["tag:noizylab-servers:3000"],
  "comment": "Developers can access development servers on port 3000"
}
```

### Testing

After applying ACLs, test connectivity:

```bash
# From a dev machine, test server access
tailscale ping noizylab-server-01

# Test SSH access
ssh noizylab-server-01

# Test database access (from appropriate tagged machine)
nc -zv noizylab-db-01 5432
```

### Troubleshooting

If connectivity fails:

1. Check device tags in admin console
2. Verify ACL rules are saved
3. Review audit logs for denied connections
4. Use the built-in ACL tests in the template

### Best Practices

1. **Start Restrictive**: Begin with minimal access and add rules as needed
2. **Use Tags**: Tag-based access scales better than per-device rules
3. **Document Changes**: Add comments to all ACL rules
4. **Test Regularly**: Use the test framework to verify rules
5. **Review Periodically**: Audit ACLs quarterly for unused rules

### References

- [Tailscale ACL Documentation](https://tailscale.com/kb/1018/acls/)
- [Tailscale SSH Documentation](https://tailscale.com/kb/1193/tailscale-ssh/)
- [NOIZYLAB Setup Guide](../CODE_MASTER/TAILSCALE_SETUP.md)
