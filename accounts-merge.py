# accounts merge
# https://neetcode.io/problems/accounts-merge/question
# code by aveia@github

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        from collections import defaultdict

        email2acc = {}
        acc2emails = defaultdict(set)
        acc2name = {}
        auto_increment = 0
        for acc in accounts:

            new_id = auto_increment
            auto_increment += 1
            acc2name[new_id] = acc[0]

            emails = acc[1:]
            for email in emails:
                email2acc[email] = new_id

                if email not in email2acc:
                    acc2emails[new_id].add(email)

                else:
                    old_id = email2acc[email]
                    if old_id == new_id:
                        continue

                    acc2emails[new_id] |= {email} | acc2emails[old_id]
                    for e in acc2emails[old_id]:
                        email2acc[e] = new_id

                    del acc2emails[old_id], acc2name[old_id]

        res = []
        for acc_id in acc2emails:
            res.append([acc2name[acc_id], *sorted(acc2emails[acc_id])])

        return res
