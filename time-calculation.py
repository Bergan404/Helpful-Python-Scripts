from datetime import datetime, timedelta

# git log --pretty=format:"%h %cd" --date=iso

# Replace the commit_log with the output from `git log` command
commit_log = """
900c005 2023-10-09 14:13:07 -0400
7137a4a 2023-02-27 07:53:45 -0500
0e2276a 2023-02-24 11:17:06 -0500
a97329d 2023-02-24 11:03:03 -0500
15ecc42 2023-02-24 10:33:42 -0500
74b646e 2023-02-24 09:52:55 -0500
04014d8 2023-02-23 16:37:26 -0500
478cb02 2023-02-23 12:00:53 -0500
4b84612 2023-02-23 11:29:23 -0500
05885a1 2023-02-23 10:41:05 -0500
09e3d9d 2023-02-23 07:13:01 -0500
31251ab 2023-02-22 15:31:23 -0500
b0f4dd4 2023-02-22 07:54:06 -0500
35c84cb 2023-02-21 16:52:23 -0500
900c005 2023-10-09 14:13:07 -0400
7137a4a 2023-02-27 07:53:45 -0500
0e2276a 2023-02-24 11:17:06 -0500
a97329d 2023-02-24 11:03:03 -0500
15ecc42 2023-02-24 10:33:42 -0500
74b646e 2023-02-24 09:52:55 -0500
04014d8 2023-02-23 16:37:26 -0500
478cb02 2023-02-23 12:00:53 -0500
4b84612 2023-02-23 11:29:23 -0500
05885a1 2023-02-23 10:41:05 -0500
09e3d9d 2023-02-23 07:13:01 -0500
31251ab 2023-02-22 15:31:23 -0500
b0f4dd4 2023-02-22 07:54:06 -0500
35c84cb 2023-02-21 16:52:23 -0500
78f7b3a 2023-02-21 09:34:56 -0500
900c005 2023-10-09 14:13:07 -0400
7137a4a 2023-02-27 07:53:45 -0500
0e2276a 2023-02-24 11:17:06 -0500
a97329d 2023-02-24 11:03:03 -0500
15ecc42 2023-02-24 10:33:42 -0500
74b646e 2023-02-24 09:52:55 -0500
04014d8 2023-02-23 16:37:26 -0500
478cb02 2023-02-23 12:00:53 -0500
4b84612 2023-02-23 11:29:23 -0500
05885a1 2023-02-23 10:41:05 -0500
09e3d9d 2023-02-23 07:13:01 -0500
31251ab 2023-02-22 15:31:23 -0500
b0f4dd4 2023-02-22 07:54:06 -0500
35c84cb 2023-02-21 16:52:23 -0500
78f7b3a 2023-02-21 09:34:56 -0500
7dbacc1 2023-02-16 16:50:46 -0500
a1bef16 2023-02-16 16:50:00 -0500
71c41af 2023-02-16 10:21:15 -0500
1cb3aca 2023-02-16 06:51:17 -0500
29947f5 2023-02-15 16:22:08 -0500
910e70d 2023-02-15 14:47:17 -0500
532f939 2023-02-15 09:18:52 -0500
f1b9e74 2023-02-15 08:03:27 -0500
877338d 2023-02-14 13:35:03 -0500
1ddaf56 2023-02-14 07:50:57 -0500
ab40f2e 2023-02-13 16:25:45 -0500
4a944f4 2023-02-13 12:55:29 -0500
12febc4 2023-02-13 10:11:18 -0500
267c2be 2023-02-11 15:05:05 -0500
c1ae8e6 2023-02-10 16:00:15 -0500
2717bb3 2023-02-10 15:52:48 -0500
a6c6a30 2023-02-10 15:37:41 -0500
ffaecb5 2023-02-10 12:14:49 -0500
df3b522 2023-02-10 11:22:00 -0500
1e7b5a0 2023-02-10 08:47:39 -0500
0dfe18c 2023-02-10 08:45:08 -0500
ae6db57 2023-02-10 08:34:46 -0500
5aa2aa8 2023-02-10 08:01:45 -0500
df0679b 2023-02-09 18:12:06 -0500
d852b8a 2023-02-09 17:53:07 -0500
ef4fa79 2023-01-20 09:37:54 -0500
adc3989 2023-01-19 15:22:49 -0500
d8e338f 2023-01-10 16:30:55 -0500
4ec08ba 2023-01-10 16:23:52 -0500
0ecf603 2023-01-10 16:06:05 -0500
c98b14f 2023-01-09 14:21:27 -0500
fc3dfb6 2023-01-09 12:15:22 -0500
1f11070 2023-01-07 13:30:04 -0500
b302027 2023-01-07 13:15:43 -0500
90b25ea 2023-01-07 12:55:30 -0500
0bc8d1e 2023-01-07 12:26:34 -0500
e77dc92 2023-01-07 12:13:08 -0500
9d8b82f 2023-01-07 11:29:14 -0500
03a2aa1 2023-01-07 10:58:55 -0500
a97b381 2023-01-07 10:44:33 -0500
9c714e7 2023-01-07 09:31:39 -0500
f2eae62 2023-01-07 08:50:32 -0500
3dab14c 2023-01-06 13:31:21 -0500
b1b2080 2023-01-06 11:21:40 -0500
6f98999 2023-01-06 08:24:11 -0500
79821ce 2023-01-06 07:44:39 -0500
"""

lines = commit_log.strip().split("\n")
total_time_hours = 0
current_date = None
first_commit_time = None
last_commit_time = None

for line in lines:
    commit_info = line.split()
    commit_hash = commit_info[0]
    commit_timestamp = " ".join(commit_info[1:3])
    commit_time = datetime.strptime(commit_timestamp, "%Y-%m-%d %H:%M:%S")

    # Get the commit date
    commit_date = commit_time.date()

    # Check if it's a new day
    if commit_date != current_date:
        if current_date is not None:
            # Calculate the time spent for the previous day
            time_diff = (last_commit_time - first_commit_time).total_seconds()
            total_time_hours += time_diff / 3600

        # Update current date and reset first and last commit times
        current_date = commit_date
        first_commit_time = commit_time

    # Update last commit time for the current day
    last_commit_time = commit_time

# Calculate the time spent for the last day if there were commits
if current_date is not None:
    time_diff = (last_commit_time - first_commit_time).total_seconds()
    total_time_hours += time_diff / 3600

workday_hours = 8
accurate_time_spent = total_time_hours / workday_hours

print("Accurate time spent: {:.2f} workdays".format(accurate_time_spent))
print("Total time spent: {:.2f} hours".format(total_time_hours))
