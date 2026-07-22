import os
import re
from datetime import datetime, timedelta

worklog_dir = "d:/Granger/fcaj-workshop-granger/fcj-workshop-template/content/1-Worklog"

def get_weekdays(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
    weekdays = []
    current = start_date
    while current <= end_date:
        if current.weekday() < 5: # 0 is Monday, 4 is Friday
            weekdays.append(current)
        current += timedelta(days=1)
    return weekdays

def process_file(filepath, is_vi):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table header to replace Time/Thời gian with Day/Thứ
    if is_vi:
        content = content.replace("| Thời gian | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |", "| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |")
        target_str = "| Cả tuần |"
    else:
        content = content.replace("| Time | Task | Start Date | Completion Date | Reference Material |", "| Day | Task | Start Date | Completion Date | Reference Material |")
        target_str = "| All week |"

    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if line.startswith(target_str):
            # parse the line
            parts = line.split('|')
            tasks_raw = parts[2].strip()
            start_date_str = parts[3].strip()
            end_date_str = parts[4].strip()
            
            # extract tasks
            tasks = [t.strip() for t in tasks_raw.split('<br>')]
            tasks = [t for t in tasks if t]
            
            weekdays = get_weekdays(start_date_str, end_date_str)
            if not weekdays:
                # Fallback if no weekdays found
                weekdays = [datetime.strptime(start_date_str, "%d/%m/%Y")]
                
            day_names_vi = ["2", "3", "4", "5", "6"]
            day_names_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            
            for i, task in enumerate(tasks):
                day_obj = weekdays[i % len(weekdays)]
                day_idx = day_obj.weekday()
                day_name = day_names_vi[day_idx] if is_vi else day_names_en[day_idx]
                date_str = day_obj.strftime("%d/%m/%Y")
                new_row = f"| {day_name} | {task} | {date_str} | {date_str} | |"
                new_lines.append(new_row)
        else:
            new_lines.append(line)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

for root, dirs, files in os.walk(worklog_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            # Skip week 1 as it's already done
            if "1.1-Week1" in filepath:
                continue
            is_vi = file.endswith('.vi.md')
            try:
                process_file(filepath, is_vi)
                print(f"Processed {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
