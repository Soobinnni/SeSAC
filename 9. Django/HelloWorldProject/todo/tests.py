from django.test import TestCase
from django.urls import reverse

from todo.models import Task


# Create your tests here.

# 실행 방법: python manage.py test todo
class TestModelTests(TestCase):
    def test_str_representation(self):
        task = Task.objects.create(title ='Test Task', description='테스트를 위한 테스크 객체')
        # if task.title == 'Test Task':
        #     print('pass')
        # else :
        #     print('fail')
        # ==
        self.assertEquals(str(task), 'Test Task')

class TestViewTests(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        print(response)
        print(response.status_code)
        print(response.content)

        # 200과 같은지
        self.assertEquals(response.status_code, 200)

        # assertTemplatedUsed : 제공된 이름의 템플릿이 렌더링에 사용되었음을 어설션
        self.assertTemplateUsed(response, 'todo/task_list.html')

    def test_task_detail_view(self):
        task = Task.objects.create(title='Test1', description='Test1111111')
        # reverse를 하지 않고 직접 ''path를 적어줄 수 있지만, 함수명으로 접근하여
        # uri경로를 불러오는 함수 == reverse이기 때문에 사용하는 것
        response = self.client.get(reverse('task_detail', args=(task.pk,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_detail.html')
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'Test1111111')

    def test_task_create_view(self):

        # get화면
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_create.html')

        data = {
            'title' : 'Test2',
            'description' : 'This is my test case 2'
        }

        # post 화면
        response = self.client.post(reverse('task_create'), data)

        # post 요청의 응답값이 redirect 로 응답 코드가 302이기 때문에
        self.assertEqual(response.status_code, 302)
        # test시 Task 모델 데이터를 하나 넣었기 때문에 안의 값이 1개 이기를 기대하기 때문에(data가 하나)
        self.assertEqual(Task.objects.count(), 1)
        
    def test_task_update_view(self):
        # task_update기능을 unit-test함수로 구현하기
        # 1. 페이지의 내용이 잘 뜨는지 확인하기
        # 2. 수정을 한 이후 안에 (db)있는 내용이 잘 반영되었는지 확인하기

        # 새 Task만듦
        task = Task.objects.create(title='Test update', description='Test update code')
        # get화면
        response = self.client.get(reverse('task_update', args=(task.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_update.html')

        # 컨텐츠까지 확인을 원하면>
        self.assertEqual(task.title, 'Test update')
        self.assertEqual(task.description, 'Test update code')

        # 업데이트 수정
        update_data = {
            'title' : 'Update Task',
            'description' : 'Update Test Again'
        }

        response = self.client.post(reverse('task_update', args=(task.pk,)), update_data)

        # 전달될 데이터가 잘 반영되었는지 확인(redirect)
        self.assertEqual(response.status_code, 302)

        # DB로부터 task 내용을 ㅐㅈ갱신
        task.refresh_from_db()
        self.assertEqual(task.title, 'Update Task')
        self.assertEqual(task.description, 'Update Test Again')

    def test_task_delete_view(self):
        # task_delete기능을 unit-test함수로 구현하기
        # 1. 새 task를 생성한다.
        # 2. 생성된 task를 삭제한다.
        # 이 내용을 어떻게? 확인할 것인지 각자 고민

        # 새 Task만듦
        task = Task.objects.create(title='Test update', description='Test update code')
        self.assertEqual(Task.objects.count(), 1) # 가상 db에 몇 개 있는 지 확인

        # 지우는 코드?
        response = self.client.post(reverse('task_delete', args=(task.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0) #지웠으니 0개

        pass
