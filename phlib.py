�
    d4�d  �                   ��  � d dl Z 	 d dlZd dlmZmZmZ n_#   ed�  �          ed�  �        Zedk    r1 e j        d�  �          e j        d�  �          e j        d�  �         n e	d	�  �         Y nxY wd dl
Zd dlZd dlmZmZmZ d
ZdZdZdZdZdZdZ e j        d�  �         dZ ee� e� e� ��  �         dZeD ] Z eedd��  �          ej        d�  �         �!d� Z e�   �          dS )�    N)�geocoder�carrier�timezonez8Please install phonenumbers library first and run again.zdo you want to install it (y/n)�yz5echo 'Instaling (phonenumbers) python with command..'zpip install phonenumberszecho 'Run tool again.'zTry again...z[34mz[30mz[31mz[32mz[36mz[33m�clearz�
        ___  _  _ ____ _  _ ____    _    _ ___  MY
        |__] |__| |  | |\ | |___ __ |    | |__]
        |    |  | |__| | \| |___    |___ | |__]
uU               [31m[46m[×][30mhttps://github.com/Mika259[31m[×][49m            

� T��end�flushg���Q��?c                  �<  � t          t          � dt          � ��  �        } t          j        d�  �         t          j        | �  �        }t          dt          � dt          � dt          j
        |d�  �        � ��  �         t          dt          � dt          � dt          j        |d�  �        � ��  �         t          dt          � d	t          � dt          j        |�  �        � ��  �         t          j        d
�  �         t          t          � dt          � ��  �        }|dk    rt!          �   �          d S |dk    r=d}|D ](}t          |dd��  �         t          j        d�  �         �)t#          �   �          d S t          t$          � dt          � ��  �         t#          �   �          d S )NzInsert Phonenumber (+60***) : g�������?u   [+]
 ╰➤ z
Location :� �enu    ╰➤ z	Carrier :z
Timezone :g      �?z
more (y/n) r   �nz [34mThanks For Using Me :)[0m
r   Tr	   g�������?zError Command!)�input�G�W�t�sleep�phonenumbers�parse�print�Yr   �description_for_numberr   �name_for_numberr   �time_zones_for_number�C�menu�exit�R)�number�phone_number�user�text1�chars        �0/data/data/com.termux/files/home/phone-lib/ph.pyr   r   +   s�  � ��!�>�>�1�>�>�?�?��	������#�)�&�1�1���d�a�d�d�1�d�d�x�/N�|�]a�/b�/b�d�d�e�e�e��V��V�V�Q�V�V��)@��t�)T�)T�V�V�W�W�W��X��X�X�a�X�X�(�*H��*V�*V�X�X�Y�Y�Y�	��������+�+��+�+�,�,���3�;�;��������S�[�[�@��!� &� &�D��d��$�7�7�7�7����������������-�-�!�-�-�.�.�.�������    )�osr   r   r   r   r   r   �want�systemr   �timer   �b�Br   r   r   r   r   �banner�textr$   r   r   � r&   r%   �<module>r0      s�  �� 
�	�	�	������9�9�9�9�9�9�9�9�9�9�9���	�E�
D�E�E�E��5�2�3�3�D��s�{�{���	�I�J�J�J���	�,�-�-�-���	�*�+�+�+�+���^��������� � � � � � � � � 5� 5� 5� 5� 5� 5� 5� 5� 5� 5��������������� 
��	�'� � � ���
 ����F��A��� � � �o��� � �D�	�E�$�B�d�#�#�#�#��A�G�D�M�M�M�M�� � �( ������s
   � �AA1