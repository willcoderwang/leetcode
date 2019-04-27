class Solution:
    def numUniqueEmails(self, emails) -> int:
        emails_modified = []
        for email in emails:
            at_index = email.index('@')
            local_name = email[:at_index]
            domain_name = email[at_index:]

            # ignore everything after first plus sign in local name
            plus_index = local_name.find('+')
            if plus_index != -1:
                local_name = local_name[:plus_index]

            # remove '.'
            local_name = ''.join([c for c in local_name if c != '.'])

            email = local_name + domain_name
            emails_modified.append(email)

        unique_emails = []
        count = 0

        for email in emails_modified:
            if email not in unique_emails:
                count += 1
                unique_emails.append(email)

        return count
