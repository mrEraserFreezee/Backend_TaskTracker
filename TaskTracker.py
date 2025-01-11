import json
import os
from datetime import datetime

FileName = 'TaskTracker.json'
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")


def load_tasks():
    if os.path.exists(FileName):
        with open(FileName, 'r') as file:
            return json.load(file)
    return[]
    
def save_tasks(tasks):
    with open(FileName, 'w') as file:
        json.dump(tasks,file)
    
def add(tasks, description):

    task={
        'id': len(tasks) + 1 ,
        'deskripsi' : description,
        'status' : 'belum dikerjakan',
        'date' : formatted_time,
        'update' : 'none'
        }

    tasks.append(task)
    save_tasks(tasks)

def display(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Deskripsi: {task['deskripsi']}, Status: {task['status']}, Date: {task.get('date')}, Update {task['update']}")

def update_task(tasks):
    task_id = int(input("Masukkan ID tugas yang ingin diupdate: "))
    status = input("Masukkan status baru (belum dikerjakan/sedang berjalan/sudah selesai): ")
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['update'] = formatted_time
            save_tasks(tasks)
            print("Tugas berhasil diupdate")
            return
    print("Tugas dengan ID tersebut tidak ditemukan")

def delate_task(tasks):
    task_id = int(input("masukan id yang ingin di hapus"))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("tugas berhasil di hapus")
            return
    print("id tidak di temukan ")

def mark_tasksdone(tasks):
    found = False
    for task in tasks:
        if task['status'] == 'sedang berjalan' or task['status'] == 'sudah selesai':
            print(f"ID: {task['id']}, Deskripsi: {task['deskripsi']}, Status: {task['status']}, Date: {task['date']}, Update {task['update']}")
            found = True
        
        if not found:
            print("belum ada pekerjaan yang dikerjakan")

def mark_notdone(tasks):
    for task in tasks:
        if task['status'] == 'belum dikerjakan':
            print(f"ID: {task['id']}, Deskripsi: {task['deskripsi']}, Status: {task['status']}, Date: {task['date']}, Update {task['update']}")

def mark_done(tasks):
    for task in tasks:
        if task['status'] == 'sudah selesai':
            print(f"ID: {task['id']}, Deskripsi: {task['deskripsi']}, Status: {task['status']}, Date: {task['date']}, Update {task['update']}")

def mark_inprogres(tasks):
    for task in tasks:
        if task['status'] == 'sedang berjalan':
            print(f"ID: {task['id']}, Deskripsi: {task['deskripsi']}, Status: {task['status']}, Date: {task['date']}, Update {task['update']}")




def main():
    tasks = load_tasks()
    while True:
        print("\n1. Tambah Tugas\n2. Tampilkan Tugas\n3. Update Tugas\n4. Hapus Tugas\n5. Keluar")
        choice = input("Pilih opsi: ")
        if choice == '1':
            description = input("Masukkan deskripsi tugas: ")
            add(tasks, description)
        elif choice == '2':
            print("Selamat datang di display Tasks Tracker\n silahkan pilih tampilan apa yang ingin anda lihat :\n1. untuk menampilkan seluruh tugas\n2. untuk menampilkan tugas yang sedang berjalan dan sudah selesai\n3. untuk menampilkan tugas yang sudah selesai\n4. untuk menampilkan tugas yang belum selesai\n5. untuk menampilkan tugas yang sedang berjalan\n6. kembali")
            choiced = input("pilih opsi : ")
            if choiced == '1':
                display(tasks)
            elif choiced == '2':
                mark_tasksdone(tasks)
            elif choiced =='3':
                mark_done(tasks)
            elif choiced == '4':
                mark_notdone(tasks)
            elif choiced == '5':
                mark_inprogres(tasks)
            elif choiced == '6':
                break
            else:
                print("pilihan tidak valid")
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delate_task(tasks)
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

