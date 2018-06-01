# Generated by Django 2.0.4 on 2018-05-31 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RBAC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=50, null=True, unique=True, verbose_name='系统编号')),
                ('asset_out_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='资产编号')),
                ('asset_name', models.CharField(max_length=100, verbose_name='资产名称')),
                ('asset_key', models.CharField(max_length=50, unique=True, verbose_name='唯一标记')),
                ('asset_description', models.TextField(null=True, verbose_name='资产介绍')),
                ('asset_score', models.IntegerField(default='0', verbose_name='重要性估值')),
                ('asset_status', models.CharField(choices=[('0', '使用中'), ('1', '闲置中'), ('2', '已销毁')], default='0', max_length=50, verbose_name='资产状态')),
                ('asset_check', models.BooleanField(default=False, verbose_name='是否检查')),
                ('asset_inuse', models.BooleanField(default=False, verbose_name='是否认领')),
                ('asset_starttime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('asset_updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='联系人邮箱')),
                ('asset_area', models.ForeignKey(limit_choices_to={'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_for_asset', to='RBAC.Area', verbose_name='所属区域')),
                ('asset_connect', models.ManyToManyField(blank=True, related_name='_asset_asset_connect_+', to='AssetManage.Asset', verbose_name='资产关联')),
            ],
        ),
        migrations.CreateModel(
            name='AssetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_key', models.CharField(max_length=30, verbose_name='申请对象')),
                ('asset_request_status', models.CharField(choices=[('0', '待审批'), ('1', '审批通过'), ('2', '审批拒绝')], default='0', max_length=30, verbose_name='状态')),
                ('request_action', models.CharField(choices=[('工作交接', '工作交接'), ('资产认领', '资产认领')], max_length=30, verbose_name='操作类型')),
                ('request_reason', models.TextField(null=True, verbose_name='申请理由')),
                ('request_note', models.TextField(null=True, verbose_name='审批备注')),
                ('request_starttime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('request_updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('action_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assetrequestaction_for_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='资产分类')),
                ('description', models.TextField(verbose_name='资产简介')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assettype_type', to='AssetManage.AssetType', verbose_name='父菜单')),
            ],
        ),
        migrations.CreateModel(
            name='AssetTypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30, null=True, unique=True, verbose_name='属性标识')),
                ('name', models.CharField(max_length=30, verbose_name='资产属性')),
                ('type_connect', models.ManyToManyField(blank=True, related_name='typeinfo_assettype', to='AssetManage.AssetType', verbose_name='属性关联')),
            ],
        ),
        migrations.CreateModel(
            name='AssetUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dst_user_email', models.EmailField(max_length=254, verbose_name='目标账号')),
                ('reason', models.TextField(verbose_name='指定说明')),
                ('asset_list', models.TextField(verbose_name='资产列表')),
                ('request_updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('action_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assetuser_action_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='附件名称')),
                ('file', models.FileField(upload_to='assetfiles/%Y/%m/%d/', verbose_name='附件内容')),
                ('file_info', models.TextField(null=True, verbose_name='附件说明')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_for_asset', to='AssetManage.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Internet_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middleware', models.CharField(blank=True, max_length=50, null=True, verbose_name='中间件')),
                ('middleware_version', models.CharField(blank=True, max_length=50, null=True, verbose_name='版本')),
                ('is_out', models.BooleanField(default=False, verbose_name='是否发布')),
                ('out_key', models.CharField(blank=True, max_length=50, null=True, verbose_name='域名')),
                ('web_status', models.CharField(choices=[('0', '测试系统'), ('1', '演示系统'), ('3', '内部使用'), ('4', '商用系统')], default='测试系统', max_length=50, verbose_name='状态说明')),
                ('language', models.CharField(choices=[('C/C++', 'C/C++'), ('C#', 'C#'), ('Ruby', 'Ruby'), ('JAVA', 'JAVA'), ('ASP.NET', 'ASP.NET'), ('JSP', 'JSP'), ('PHP', 'PHP'), ('Perl', 'Perl'), ('Python', 'Python'), ('VB.NET', 'VB.NET'), ('Other', 'Other')], max_length=50, null=True, verbose_name='开发语言')),
                ('language_version', models.CharField(blank=True, max_length=50, null=True, verbose_name='语言版本')),
                ('web_framwork', models.CharField(blank=True, max_length=50, null=True, verbose_name='开发框架')),
                ('web_framwork_version', models.CharField(blank=True, max_length=50, null=True, verbose_name='开发框架版本')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='internet_for_asset', to='AssetManage.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='OS_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='主机名')),
                ('os', models.CharField(blank=True, max_length=100, verbose_name='操作系统')),
                ('vendor', models.CharField(blank=True, max_length=50, verbose_name='设备厂商')),
                ('cpu_model', models.CharField(blank=True, max_length=100, verbose_name='CPU型号')),
                ('cpu_num', models.CharField(blank=True, max_length=100, verbose_name='CPU数量')),
                ('memory', models.CharField(blank=True, max_length=30, verbose_name='内存大小')),
                ('disk', models.CharField(blank=True, max_length=255, verbose_name='硬盘大小')),
                ('monitor', models.CharField(blank=True, max_length=30, verbose_name='监控关联')),
                ('sn', models.CharField(blank=True, max_length=60, verbose_name='SN号 码')),
                ('cabinet', models.CharField(blank=True, max_length=50, verbose_name='机柜信息')),
                ('up_time', models.DateField(null=True, verbose_name='上架时间')),
                ('guarante_time', models.DateField(null=True, verbose_name='保修时间')),
                ('down_time', models.DateField(null=True, verbose_name='停用时间')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='os_for_asset', to='AssetManage.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Plugin_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='组件名称')),
                ('version', models.CharField(max_length=50, null=True, verbose_name='应用版本')),
                ('plugin_info', models.TextField(null=True, verbose_name='组件简介')),
                ('starttime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_for_asset', to='AssetManage.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Port_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='开放端口')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='服务名称')),
                ('product', models.CharField(max_length=100, null=True, verbose_name='产品信息')),
                ('version', models.CharField(max_length=50, null=True, verbose_name='应用版本')),
                ('port_info', models.TextField(null=True, verbose_name='端口介绍')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='port_for_asset', to='AssetManage.Asset')),
            ],
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='asset_type',
            field=models.ForeignKey(limit_choices_to={'parent__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_for_assetrequest', to='AssetManage.AssetType', verbose_name='资产类型'),
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='request_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assetrequest_for_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(limit_choices_to={'parent__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_for_asset', to='AssetManage.AssetType', verbose_name='资产类型'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_user',
            field=models.ManyToManyField(blank=True, related_name='asset_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]