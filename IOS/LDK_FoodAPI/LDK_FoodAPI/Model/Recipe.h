//
//  Recipe.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Recipe : NSObject

@property (strong, nonatomic) NSString *publisher;
@property (strong, nonatomic) NSString *f2fUrl;
@property (strong, nonatomic) NSString *title;
@property (strong, nonatomic) NSString *sourceUrl;
@property (strong, nonatomic) NSString *recipeId;
@property (strong, nonatomic) NSString *imageUrl;
@property (strong, nonatomic) NSNumber *socialRank;
@property (strong, nonatomic) NSString *publisherUrl;

+ (Recipe *)recipeFromDictionary:(NSDictionary *)recipeDict;

@end
